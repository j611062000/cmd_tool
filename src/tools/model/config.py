import configparser

class Config():
    def __init__(self, is_enable_cache: bool = False) -> None:
        self.is_enable_cache: bool = is_enable_cache
    
    def update_from_config(self, config: configparser.ConfigParser) -> None:
        self.is_enable_cache = config.getboolean("general", "is_enable_cache")