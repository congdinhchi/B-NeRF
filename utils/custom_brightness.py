import imageio
import json
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image
import random

# Đường dẫn đến file ảnh
data_path ="./data/processed/lego/train"
list_img_path = []
for img_path in glob(f"{data_path}/*"):

    list_img_path.append(img_path)

name_type = data_path.split("/")[-1]
new_data_path = data_path.replace(name_type, f"new_{name_type}")
if os.path.exists(new_data_path):
    shutil.rmtree(new_data_path)
os.mkdir(new_data_path)

list_data =[]

for img_path in list_img_path:
    # Đọc ảnh
    data = {}
    image = imageio.imread(img_path)
    data["file_path"] = img_path
    # Tăng/giảm độ sáng bằng cách thêm/sử dụng một giá trị cộng thêm
    brightness_factor = random.uniform(0.3, 1.5)  # Giá trị > 1 tăng độ sáng, < 1 giảm độ sáng
    # transforms_train
    data["shutter_speed"] = brightness_factor

    # Thay đổi độ sáng của ảnh
    brightened_image = np.clip(image.astype(np.float32) * brightness_factor, 0, 255).astype(np.uint8)

    # Hiển thị ảnh gốc và ảnh đã thay đổi độ sáng
    name_type = img_path.split("/")[-2]
    output_path = img_path.replace(name_type, f"new_{name_type}")
    imageio.imwrite(output_path,brightened_image)

    list_data.append(data)

# transforms_train
with open(f'./data/processed/lego/log_shutter_speed.json', 'w') as file_ra:
    json.dump(list_data, file_ra)
