import cv2
from glob import glob
import os
import shutil

image_path = ".\\data\\B_nerf_random"

def split_image(image, start, end, name_img):
    new_image = image[:, start:end]
    cv2.imwrite(name_img, new_image)

# Gọi hàm cắt ảnh
if __name__=="__main__":

    new_path = f"{image_path}_new"
    if os.path.exists(new_path):
        shutil.rmtree(new_path)
    os.mkdir(new_path)

    list_img_path = glob(f"{image_path}\\*")
    j = 0 
    for image_path in list_img_path:
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        start = 220
        end = 720
        for i in range(0,3):
            if i == 0:
                name_img = f"{new_path}\\novel_view_{j}.png"
            elif i == 1:
                name_img = f"{new_path}\\depth_map_{j}.png"
            else:
                name_img = f"{new_path}\\log_{j}.png"
            
            split_image(image, start, end, name_img)
            start = end+20
            end += 550
        j+=5