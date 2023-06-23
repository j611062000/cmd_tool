import configparser
from model.config import Config

__app_name__ = "price_getter"
__version__ = "0.1.0"

config_path = "./price_getter/config.ini"
config_instance: Config = Config()


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}


config = configparser.ConfigParser()
config.read(config_path) 
config_instance.update_from_config(config)
