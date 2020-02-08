import configparser
import logging
import os
config = configparser.ConfigParser()
path = os.path.abspath(os.path.dirname(__file__)) + os.sep+'props.ini'
config.read(path)
print(config.sections())

logging.basicConfig(level=logging.INFO)


def get_url():
    return config['api']['url'] + config['api']['current_id']


def update_props(id):
    config['api']['current_id'] = str(id)
    with open(path, 'w') as conf_file:
        config.write(conf_file)
