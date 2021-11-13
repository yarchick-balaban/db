import pymysql.cursors
import csv
from datetime import datetime as dt


# Request string to retrieve from the database name, mail, phone number from the database
QUERY = 'SELECT `firstname`, `lastname`, `email`, `telephone` FROM `oc_customer`'

class DBWriteToFile:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def start(self):
        get_connect = self.get_connections_to_db(self.host, self.user, self.password, self.db)
        extract_data = self.get_from_db(get_connect)
        write_data_to_file = self.write_to_file(extract_data)

    def get_connections_to_db(self, host, user, password, db):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        return connection

    def get_from_db(self, connection):
        with connection as conn:
            cur = conn.cursor()
            query = QUERY
            cur.execute(query)
            rows = cur.fetchall()
            print(type(rows))
            result = []
            for i in rows:
                i['Имя'] = i.pop('firstname')
                i['Фамилия'] = i.pop('lastname')
                i['Почта'] = i.pop('email')
                i['Телефон'] = i.pop('telephone')
                result.append(i)
            return result

    def write_to_file(self, result):
        __now = dt.now()
        csv_column_order = list(result[0].keys())
        with open(f'exported_{__now.strftime("%H-%M-%S")}.csv', 'a', newline='') as csvfile:
            myCsvWriter = csv.DictWriter(csvfile, delimiter=',',
                                         quotechar='"',
                                         fieldnames=csv_column_order)

            myCsvWriter.writeheader()
            for row in result:
                myCsvWriter.writerow(row)
