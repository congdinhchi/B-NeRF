import configparser
from src.const.path import CONFIG_PATH
from loguru import logger
import sys
import os

file_config = os.path.join(CONFIG_PATH, "view.ini")

config = configparser.ConfigParser()
config.read(file_config)
level_log = str(config['LOG']['level'])

logger.remove()
logger.add(sink=sys.stderr, level=level_log)