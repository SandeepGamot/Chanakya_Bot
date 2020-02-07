import configparser


config = configparser.ConfigParser()
config.read('props.ini')
print(config.sections())

def build_url():
    return config['api']['url'] + config['api']['current_id']


def update_props():
    config['api']['current_id'] = str(int(config['api']['current_id']) + 1)
    with open('props.ini', 'w') as conf_file:
        config.write(conf_file)
