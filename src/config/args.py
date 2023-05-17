import argparse
import configparser
import os 
from src.lib.loguru import logger
from src.const.path import CONFIG_PATH
import tensorflow as tf

class ConfArgs:

    @staticmethod
    def get_args_user():
        # config by user
        parser = argparse.ArgumentParser(description= "Menu B-NeRF")

        parser.usage = "User manual B-NeRF"

        parser.add_argument("--case", metavar="case name", type=str, help="./processed/<case_name>")
        parser.add_argument("--continue_training", metavar="continue training from", type=str, help="./processed/<case_name>/record/<name_record>")
        # parser.add_argument("-c", '--continue_training', help="is continue training", action="store_true")

        args = parser.parse_args()
        
        return args

    @staticmethod
    def get_args_model():
        # config by model
        config = configparser.ConfigParser()
        file_config_path = os.path.join(CONFIG_PATH, "model.ini")
        config.read(file_config_path) #epoch = config['model']['epoch']
        args_model = dict(config["model"])

        # add
        args_model["auto"] = tf.data.AUTOTUNE
        return args_model