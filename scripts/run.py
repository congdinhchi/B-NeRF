from src.log.loguru import logger
from src.config.args import ConfArgs
from src.const.path import *
from src.data.manager import DataManager
import numpy as np
import tensorflow as tf
import os

if __name__ == "__main__":
    logger.debug("Starting B-NeRF")
    
    # get config info
    args_user = ConfArgs.get_args_user()
    args_model = ConfArgs.get_args_model()

    # set params
    random_seed = int(args_model["model"]["random_seed"])
    np.random.seed(random_seed)
    tf.random.set_seed(random_seed)

    # load data
    data_path = os.path.join(DATA_PROCESS_PATH, args_user.case)
    data_model = DataManager(data_path)
    list_image_path = data_model.get_images_path()
    
    
