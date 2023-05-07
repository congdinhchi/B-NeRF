from src.lib.loguru import logger
from src.config.args import ConfArgs
from src.const.path import *
from src.data.manager import DataManager
import numpy as np
import tensorflow as tf
import os

def set_params(random_seed):
    np.random.seed(random_seed)
    tf.random.set_seed(random_seed)

def train(args_user, args_model) -> None:
    
    # load data
    try:
        data_path = os.path.join(DATA_PROCESS_PATH, args_user.case)
        data_model = DataManager(data_path)
    except:
        logger.error("No name case! You need add --case <case_name> in terminal")

    if args_user.continue_training is None:
        logger.info(f"Starting train ...")
    else:
        logger.info("Continue train")

if __name__ == "__main__":
    logger.debug("Starting B-NeRF")
    
    # get args info
    args_user = ConfArgs.get_args_user()
    args_model = ConfArgs.get_args_model()

    # set params
    random_seed = int(args_model["model"]["random_seed"])
    set_params(random_seed)

    # train
    train(args_user, args_model)
    

    

    
