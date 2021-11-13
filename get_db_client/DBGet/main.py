from get_db_client.DBGet.wrok_folder.client_from_db_to_csv import getDBWriteToFile
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
<<<<<<< HEAD
    write_from_db_to_file = DBWriteToFile(
=======
    write_from_db_to_file = getDBWriteToFile(
>>>>>>> bdc907c2dd7ed153b609708c785636c16cf4cd96
        host=config.get('mysql', 'host'),
        user=config.get('mysql', 'user'),
        password=config.get('mysql', 'password'),
        db=config.get('mysql', 'db'))
    write_from_db_to_file.start()
