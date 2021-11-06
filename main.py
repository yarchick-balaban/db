import pymysql, configparser
import pymysql.cursors
import csv

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')


connection = pymysql.connect(
    host=config.get('mysql', 'host'),
    user=config.get('mysql', 'user'),
    password=config.get('mysql', 'password'),
    db=config.get('mysql', 'db'),
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection as conn:
    cur = conn.cursor()
    with open('sql-balleon.sql', 'r') as inserts:
        query = inserts.read()
    cur.execute(query)
    rows = cur.fetchall()
    result = []
    cont = 0
    for i in rows:
        i = rows[cont]
        i['Имя'] = i.pop('firstname')
        i['Фамилия'] = i.pop('lastname')
        i['Почта'] = i.pop('email')
        i['Телефон'] = i.pop('telephone')
        result.append(i)
        cont += 1


    csv_column_order = list(result[0].keys())
    with open('exported.csv', 'w', newline='') as csvfile:
        myCsvWriter = csv.DictWriter(csvfile, delimiter=',',
                                          quotechar='"',
                                          fieldnames = csv_column_order)

        myCsvWriter.writeheader()
        for row in result:
            myCsvWriter.writerow(row)