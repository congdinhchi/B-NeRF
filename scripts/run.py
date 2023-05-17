from src.lib.loguru import logger
from src.config.args import ConfArgs
from src.const.path import *
from src.data.manager import DataManager
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt 
import cv2

def set_params(random_seed):
    np.random.seed(random_seed)
    tf.random.set_seed(random_seed)

def train(args_user, args_model) -> None:
    
    # load data
    if args_user.case == None:
        logger.error("No name case! You need add --case <case_name> in terminal")
        return 
    
    data_path = os.path.join(DATA_PROCESS_PATH, args_user.case)
    data_model = DataManager(data_path)
    images, pose = data_model.get_data()
    print(f"pose {images[0]}")
    print(f"pose {pose[0]}")

def continue_train(args_user, args_model):
    pass

if __name__ == "__main__":
    logger.info("B-NeRF")
    
    # get args info
    args_user = ConfArgs.get_args_user()
    args_model = ConfArgs.get_args_model()

    # set params
    random_seed = int(args_model["random_seed"])
    set_params(random_seed)

    # train
    if args_user.continue_training is None:
        logger.debug(f"Starting train ...")
        train(args_user, args_model)
    else:
        logger.debug("Continue train")
    
    

    

    
