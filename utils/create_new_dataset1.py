# tao data set thay doi so luong anh

import imageio

import shutil
import numpy as np
from glob import glob
import os
import shutil
from PIL import Image
import random
import json

# Đường dẫn đến file ảnh
data_path ="./data/processed/random_b/train"
list_img_path = []
for img_path in glob(f"{data_path}/*"):
    list_img_path.append(img_path)



# Read file json

# Mở file JSON để đọc
with open('./data/processed/random_b/transforms_train.json') as file:
    data = json.load(file)
    new_data = {}
    new_data["camera_angle_x"] = data["camera_angle_x"]

    frames = list(data["frames"])
    new_frames = []
    number_new_images = 0
    list_img = []
    for frame in frames:
        new_fame = {}
        value = dict(frame)
        
        index_image = int(value["file_path"].split("_")[-1])

        if index_image%2 == 0 or index_image%11== 0 or index_image%3==0:
            new_fame["file_path"] = value["file_path"]
            list_img.append(value["file_path"])
            new_fame["rotation"] = value["rotation"]
            new_fame["transform_matrix"] = value["transform_matrix"]
            
            number_new_images += 1
            new_frames.append(new_fame)
    
    new_data["frames"] = new_frames



# Root path
path_root = f"./data/processed/{number_new_images}"
try:
    os.mkdir(path_root)
except:
    shutil.rmtree(path_root)
    os.mkdir(path_root)

# train folder
os.mkdir(f"{path_root}/train")
for path in list_img:
    old_path = path.replace("./train", data_path)
    old_path = f"{old_path}.png"

    new_path = path.replace(".", path_root)
    new_path = f"{new_path}.png"

    shutil.copy(old_path, new_path)
    

# transforms_train
with open(f'{path_root}/transforms_train.json', 'w') as file_ra:
    json.dump(new_data, file_ra)

# val
old_val_path = data_path.replace("train", "val")
new_val_path = f"{path_root}/val"
shutil.copytree(old_val_path, new_val_path)

old_val_json =  data_path.replace("train", "transforms_val.json")
new_val_json = f"{path_root}/transforms_val.json"
shutil.copy(old_val_json, new_val_json)

#test 
old_test_path = data_path.replace("train", "test")
new_test_path = f"{path_root}/test"
shutil.copytree(old_test_path, new_test_path)

old_test_json =  data_path.replace("train", "transforms_test.json")
new_test_json = f"{path_root}/transforms_test.json"
shutil.copy(old_test_json, new_test_json)
