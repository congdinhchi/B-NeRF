from src.log.loguru import logger
from src.config.args import ConfArgs

if __name__ == "__main__":
    logger.debug("Starting B-NeRF")
    
    conf_args = ConfArgs()
    args_user = conf_args.get_args_user()
    args_model = conf_args.get_args_model()

    print(args_model["model"]["random_seed"])
