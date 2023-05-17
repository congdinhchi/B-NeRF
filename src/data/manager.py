import os 
from glob import glob
import json
from src.const.path import *
from src.model.image import ImageModel
class DataManager():
    '''info folder data processed'''
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path
        self.images_path = os.path.join(data_path, "images")
        self.transform_path = os.path.join(data_path, "transforms.json")

    def get_data(self) :
        '''get info from file transforms.json'''
        # Đọc tệp tin JSON
        with open(self.transform_path, 'r') as file:
            data = json.load(file)

        # Đọc dữ liệu 
        datasetPath = self.data_path
        imagePaths = []
        c2ws = []
        
        for frame in data["frames"]:
            imagePath = frame["file_path"]
            imagePath = imagePath.replace(".", datasetPath)
            imagePath = f"{imagePath}.png"
            imagePaths.append(imagePath)
            
            c2w = frame["transform_matrix"]
            c2ws.append(c2w)
            
        
        return imagePaths,c2ws
