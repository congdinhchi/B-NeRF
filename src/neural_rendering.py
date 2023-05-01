import torch

class NeuralRendering:

    @staticmethod
    def neural2images(
        raw: torch.Tensor,
        z_vals: torch.Tensor,
        rays_d: torch.Tensor,
        raw_noise_std: float = 0.0,
        white_bkgd: bool = False
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        r"""
        Chuyển đổi kết quả mạng neural về ảnh 2d
        raw: [n_rays, n_samples, 4] số 4 là giá trị RGB và mật độ
        z_vals: [n_rays, n_samples] Danh sách khoảng cách các điểm trên tia so với điểm gốc 
        rays_d: (number_ray, 3) với number_ray là số lượng tia, 3 là không gian 3d
        raw_noise_std: 
        white_bkgd: nền trắng hay đen
        """

        # Tính khoảng cách giữa các điểm trên tia so với điểm gốc
        dists = z_vals[..., 1:] - z_vals[..., :-1]
        dists = torch.cat([dists, 1e10 * torch.ones_like(dists[..., :1])], dim=-1) # Nối thêm khoảng cách đại diện cho điểm cuối cùng

        # Chuẩn hóa khoảng cách theo hướng của tia
        magnitude = torch.norm(rays_d[..., None, :], dim=-1) # Tính độ lớn vector vô hướng cho từng tia (num_ray, 3) -> (num_ray, 1, 3) -> (num_ray, 1), thêm None vào để có số chiều đầu ra đúng với list_dist
        list_dist = list_dist * magnitude

        # Add noise to model's predictions for density. Can be used to 
        # regularize network during training (prevents floater artifacts).
        noise = 0.
        if raw_noise_std > 0.:
            noise = torch.randn(raw[..., 3].shape) * raw_noise_std

        # Predict density of each sample along each ray. Higher values imply
        # higher likelihood of being absorbed at this point. [n_rays, n_samples]
        alpha = 1.0 - torch.exp(-nn.functional.relu(raw[..., 3] + noise) * dists)

        # Compute weight for RGB of each sample along each ray. [n_rays, n_samples]
        # The higher the alpha, the lower subsequent weights are driven.
        weights = alpha * cumprod_exclusive(1. - alpha + 1e-10)

        # Compute weighted RGB map.
        rgb = torch.sigmoid(raw[..., :3])  # [n_rays, n_samples, 3]
        rgb_map = torch.sum(weights[..., None] * rgb, dim=-2)  # [n_rays, 3]

        # Estimated depth map is predicted distance.
        depth_map = torch.sum(weights * z_vals, dim=-1)

        # Disparity map is inverse depth.
        disp_map = 1. / torch.max(1e-10 * torch.ones_like(depth_map),
                                    depth_map / torch.sum(weights, -1))

        # Sum of weights along each ray. In [0, 1] up to numerical error.
        acc_map = torch.sum(weights, dim=-1)

        # To composite onto a white background, use the accumulated alpha map.
        if white_bkgd:
            rgb_map = rgb_map + (1. - acc_map[..., None])

        return rgb_map, depth_map, acc_map, weights
