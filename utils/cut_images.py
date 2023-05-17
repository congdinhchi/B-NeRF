import cv2
from glob import glob
import os
import shutil
from tqdm import tqdm
#config
data_path = "..\\data\\raw\\crane"

area = 1000

if __name__ == "__main__":
    '''Crop ảnh tự động'''

    list_image = glob(f"{data_path}\\images\\*")

    new_images_path = f"{data_path}//new_images"
    if os.path.exists(new_images_path):
        shutil.rmtree(new_images_path)
    os.makedirs(new_images_path)

        # Tạo thanh loading động
    for image_path in tqdm(list_image):
        image = cv2.imread(image_path)
        name_img = os.path.basename(image_path)

        # Lấy thông tin về số chiều
        height, width, channels = image.shape
        y_center = height//2
        x_center = width//2

        x_top = x_center - area
        y_top = y_center - area
        x_bot = x_center + area
        y_bot= y_center + area

        # Áp dụng phép cắt
        cropped_image = image[y_top:y_bot, x_top:x_bot]

        # Hiển thị ảnh gốc và ảnh đã cắt
        new_path = f"{new_images_path}//{name_img}"
        cv2.imwrite(new_path, cropped_image)