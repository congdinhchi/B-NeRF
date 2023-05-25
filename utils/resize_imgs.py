from PIL import Image
import os
from glob import glob
import shutil

# config
data_path = ".\\data\\raw\\lego"
type_data = "train"
new_size = (300,300)

find_path = os.path.join(data_path, type_data, "*")

new_folder =  os.path.join(data_path, f"new_{type_data}")
if os.path.exists(new_folder):
    shutil.rmtree(new_folder)
os.mkdir(new_folder)


list_imgs = glob(find_path)
for image_path in list_imgs:
    print(image_path)
    # Mở ảnh gốc
    image = Image.open(image_path)

    # Resize ảnh về kích thước mới (300x300)
    resized_image = image.resize(new_size)

    # Lưu ảnh resized
    name_img = os.path.basename(image_path)
    new_path = os.path.join(new_folder, name_img)
    resized_image.save(new_path)