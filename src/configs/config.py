import configparser
import pathlib

def get_token(section: str = 'Telegram', attribute: str = 'token'):
    conf_file_path = pathlib.Path(__file__).parent.absolute().joinpath('tm_config.ini')
    config = configparser.ConfigParser()
    config.read(conf_file_path)
    return config[section][attribute]