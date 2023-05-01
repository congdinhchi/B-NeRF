import torch

class PositionalEncoder():

    def __init__(self, d_input: int, l: int) -> None:
        '''
        d_input: dimention input
        l: Sô lượng tần số (L trong bai bao)
        '''
        freq_bands = 2.**torch.linspace(0., l - 1, l)
        self.embed_fns = [lambda x:x] # bias
        for freq in freq_bands:
            self.embed_fns.append(lambda x, freq=freq: torch.sin(x * freq))
            self.embed_fns.append(lambda x, freq=freq: torch.cos(x * freq))

    def encode(self, x) -> torch.Tensor:
        r"""
        Mã hóa
        """
        list_value = [fn(x) for fn in self.embed_fns]
        print(f"list_value {list_value}")
        return torch.concat(list_value, dim=-1)

# test
if __name__ == "__main__":
    ps_function = PositionalEncoder(3, 2)
    x = torch.tensor([3.0, 4.0, 5.0])
    result = ps_function.encode(x)
    print(result)