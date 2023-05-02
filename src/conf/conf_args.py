import argparse
import configparser


class ConfArgs:

    @staticmethod
    def get_args_user():
        # config by user
        parser = argparse.ArgumentParser(description= "Menu B-NeRF")

        parser.usage = "User manual B-NeRF"

        parser.add_argument("--name_method", metavar="name_method", type=str, help="method choice")
        parser.add_argument("-c", '--continue_training', help="is continue training", action="store_true")

        args = parser.parse_args()
        return args

    @staticmethod
    def get_args_system():
        # config by system
        config = configparser.ConfigParser()
        config.read('./conf/model.ini') #epoch = config['model']['epoch']
        
        return config
    