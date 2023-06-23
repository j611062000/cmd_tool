import configparser

class Config():
    def __init__(self, is_enable_cache: bool = False, twse_api:str = "") -> None:
        self.is_enable_cache: bool = is_enable_cache
        self.twse_api_endpoint: str = twse_api
    
    def update_from_config(self, config: configparser.ConfigParser) -> None:
        self.is_enable_cache = config.getboolean("general", "is_enable_cache")
        self.twse_api_endpoint = config.get("dependency", "twse_api_endpoint")