import json
import os

#config
data_path = ".\\data\\raw\\crane"

if __name__ == "__main__":
    camera_pose_path = os.path.join(data_path, "dataShot.json")
    with open(camera_pose_path, 'r') as file:
            camera_pose = json.load(file)

    x = camera_pose[0]['ObjPosX']
    y = camera_pose[0]['ObjPosY']
    z = camera_pose[0]['ObjPosZ']
    list_x = [x]*len(camera_pose)
    list_y = [y]*len(camera_pose)
    list_z = [z]*len(camera_pose)

    x_points = []
    y_points = []
    z_points = []
    
    for info_image in camera_pose:
        x = info_image['CamPosX']
        y = info_image['CamPosY']
        z = info_image['CamPosZ']
        
        x_points.append(x)
        y_points.append(y)
        z_points.append(z)
    
    direction()