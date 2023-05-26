import cv2
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image

# Đường dẫn đến file ảnh
data_path =".\\data\\raw\\lego2\\images"
list_img_path_1 = glob(f"{data_path}\\*")

list_img_path = []
list_depth = []
for img_path in list_img_path_1:
    if "depth" in img_path:
        list_depth.append(img_path)
    else:
        list_img_path.append(img_path)

name_type = data_path.split("\\")[-1]
new_data_path = data_path.replace(name_type, f"new_{name_type}")
if os.path.exists(new_data_path):
    shutil.rmtree(new_data_path)
os.mkdir(new_data_path)

for img_path in list_img_path:
    # Đọc ảnh
    image = Image.open(img_path)
    # Chuyển ảnh thành mảng numpy
    image = np.array(image)

    # Độ sáng ngẫu nhiên
    brightness_factor = np.random.uniform(0.5, 1.5)

    # Áp dụng thay đổi độ sáng lên ảnh
    brightened_image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)

    # Hiển thị ảnh gốc và ảnh đã thay đổi độ sáng
    name_type = img_path.split("\\")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}")
    brightened_image = Image.fromarray(brightened_image)
    brightened_image.save(output_path)

for img_path in list_depth:
    name_type = img_path.split("\\")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}") 
    shutil.move(img_path, output_path)