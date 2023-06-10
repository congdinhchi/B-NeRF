from PIL import Image
import json
import numpy as np
import os
import glob

data_path = '.\\data\\transforms.json'
with open(data_path, 'r') as file:
  data = json.load(file)
  # Đọc dữ liệu
  for i in range(len(data["frames"])):
    frame = data["frames"][i]
    print(frame)