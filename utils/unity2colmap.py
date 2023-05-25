from PIL import Image
import os
from glob import glob
import shutil

# config
data_path = ".\\data\\raw\\shoe2"
type_data = "images"

find_path = os.path.join(data_path, type_data, "*")

list_imgs = glob(find_path)
for image_path in list_imgs:
    if "meta" in image_path:
        print(f"remove {image_path}")
        os.remove(image_path)