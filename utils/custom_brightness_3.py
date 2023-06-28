import cv2
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image
import OpenEXR

# Đường dẫn đến file ảnh
data_path ="./data/processed/lego/train"
list_img_path_1 = glob(f"{data_path}/*")

list_img_path = []
list_depth = []
for img_path in list_img_path_1:
    if "depth" in img_path:
        list_depth.append(img_path)
    else:
        list_img_path.append(img_path)

name_type = data_path.split("/")[-1]
new_data_path = data_path.replace(name_type, f"new_{name_type}")
if os.path.exists(new_data_path):
    shutil.rmtree(new_data_path)
os.mkdir(new_data_path)

for img_path in list_img_path:
    # Đọc ảnh
    image = np.array(Image.open(img_path).convert('RGB')) 

    # Độ sáng ngẫu nhiên
    brightness_factor = np.random.uniform(0.7, 1.3)

    # Áp dụng thay đổi độ sáng lên ảnh
    brightened_image = np.clip(image * brightness_factor, 0, 255).astype(np.float32)

    # Hiển thị ảnh gốc và ảnh đã thay đổi độ sáng
    name_type = img_path.split("/")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}")
    brightened_image = Image.fromarray(brightened_image)
    
    brightened_image.save(output_path)
    # Tạo một đối tượng Image giữ các kênh màu RGB
    exr_image = OpenEXR.OutputFile('output_image.exr', OpenEXR.Header(image_rgb.shape[1], image_rgb.shape[0]))

    # Ghi dữ liệu vào từng kênh màu
    exr_image.writePixels({'R': image_rgb_float32[:,:,0].tobytes(),
                        'G': image_rgb_float32[:,:,1].tobytes(),
                        'B': image_rgb_float32[:,:,2].tobytes()})

# Đóng tệp tin EXR
exr_image.close()

for img_path in list_depth:
    name_type = img_path.split("/")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}") 
    shutil.move(img_path, output_path)