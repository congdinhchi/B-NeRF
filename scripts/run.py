from loguru import logger
from src.conf.conf_args import ConfArgs

if __name__ == "__main__":
    logger.info("Starting B-NeRF")
    
    conf_args = ConfArgs()
    args_system = conf_args.get_args_system()
    args_user = conf_args.get_args_user()

    print(args_user.name_method)
