from loguru import logger
from src.conf.conf_args import ConfArgs

if __name__ == "__main__":
    logger.info("Starting B-NeRF")
    
    conf_args = ConfArgs()
    args = conf_args.get_args_user()
    conf = conf_args.get_args_system()


