import cv2
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image
import random
import imageio

def adjust_gamma(image):
    gamma = random.uniform(0.2, 1.5) 
    # Tính toán bảng gamma correction
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype(np.uint8)
	# apply gamma correction using the lookup table
    return cv2.LUT(image, table)


# Đường dẫn đến file ảnh
data_path ="./data/processed/lego/train"
list_img_path_1 = glob(f"{data_path}/*")

list_img_path = []

for img_path in list_img_path_1:
    list_img_path.append(img_path)

name_type = data_path.split("/")[-1]
new_data_path = data_path.replace(name_type, f"new_{name_type}")
if os.path.exists(new_data_path):
    shutil.rmtree(new_data_path)
os.mkdir(new_data_path)

for img_path in list_img_path:
    
    # Đọc ảnh
    image = imageio.imread(img_path)

    tmp = img_path.split("_")[-1]
    
    brightened_image = adjust_gamma(image)

    # Hiển thị ảnh gốc và ảnh đã thay đổi độ sáng
    name_type = img_path.split("/")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}")

    imageio.imwrite(output_path,brightened_image)
