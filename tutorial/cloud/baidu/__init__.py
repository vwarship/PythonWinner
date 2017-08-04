import configparser


CONFIG_FILENAME = 'key.conf'
config = configparser.ConfigParser()
config.read(CONFIG_FILENAME)


def get_key_values(key):
    APP_ID = config[key]['APP_ID']
    API_KEY = config[key]['API_KEY']
    SECRET_KEY = config[key]['SECRET_KEY']

    return (APP_ID, API_KEY, SECRET_KEY)
