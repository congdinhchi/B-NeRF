import hydra
import argparse

class ConfArgs:

    @staticmethod
    @hydra.main(config_path="../../conf", config_name="model")
    def get_args_system(cfg):
        # config by system
        print(cfg["params"]["name_model"])

    @staticmethod
    def get_args_user():
        # config by user
        parser = argparse.ArgumentParser(description= "Menu B-NeRF")

        parser.usage = "User manual B-NeRF"

        parser.add_argument("--name_method", metavar="name_method", type=str, help="method choice")
        parser.add_argument("-c", '--continue_training', help="is continue training", action="store_true")

        args = parser.parse_args()
        return args