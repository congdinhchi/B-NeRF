import cv2

class ImageModel():

    def __init__(self, imgPath, pose) -> None:
        self.imgPath = imgPath
        self.image = cv2.imread(imgPath)
        self.pose = pose

    def get_image(self):
        return self.image
    
    def get_pose(self):
        return self.pose