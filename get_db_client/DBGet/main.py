from get_db_client.DBGet.wrok_folder.client_from_db_to_csv import getConnect
import configparser

#The folder should contain a configuration file in a standard form:
# [mysql]
# host = localhost
# database = python_mysql
# user = root
# password =
CONFIG_FILE_PATH = '../config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH, encoding='utf-8-sig')

if __name__ == "__main__":
    get_db = getConnect(
        host=config.get('mysql', 'host'),
        user=config.get('mysql', 'user'),
        password=config.get('mysql', 'password'),
        db=config.get('mysql', 'db'))
    get_db.connections()
