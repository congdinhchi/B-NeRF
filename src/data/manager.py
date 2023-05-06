import os 
from glob import glob

class DataManager():
    '''info folder data processed'''
    def __init__(self, data_path: str) -> None:
        self.images_path = os.path.join(data_path, "images")
        self.transform_path = os.path.join(data_path, "transforms.json")

    def get_images_path(self) -> list:
        # get all list images path
        images_path = os.path.join(self.images_path , "*")
        return glob(images_path)
