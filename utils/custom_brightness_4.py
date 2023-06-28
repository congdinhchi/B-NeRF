import cv2
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
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
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Độ sáng ngẫu nhiên
    brightness_factor = 1

    

    # Hiển thị ảnh gốc và ảnh đã thay đổi độ sáng
    name_type = img_path.split("/")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}")
    output_path = img_path.replace(".png", ".exr")
    # Chuyển đổi ảnh thành dạng EXR
    cv2.imwrite(output_path, image)
