import pymysql.cursors
import csv

class getConnect:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connections(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.get_query(connection)

    def get_query(self, connection):
        with connection as conn:
            cur = conn.cursor()
            query = 'SELECT `firstname`, `lastname`, `email`, `telephone` FROM `oc_customer`'
            cur.execute(query)
            rows = cur.fetchall()
            result = []
            cont = 0
            for i in rows:
                i['Имя'] = i.pop('firstname')
                i['Фамилия'] = i.pop('lastname')
                i['Почта'] = i.pop('email')
                i['Телефон'] = i.pop('telephone')
                result.append(i)
                cont += 1
            self.write_to_file(result)

    def write_to_file(self, result):
        csv_column_order = list(result[0].keys())
        with open('exported.csv', 'w', newline='') as csvfile:
            myCsvWriter = csv.DictWriter(csvfile, delimiter=',',
                                         quotechar='"',
                                         fieldnames=csv_column_order)

            myCsvWriter.writeheader()
            for row in result:
                myCsvWriter.writerow(row)
