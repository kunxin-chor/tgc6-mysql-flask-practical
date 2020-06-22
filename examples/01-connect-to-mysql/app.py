import pymysql
import os


def get_connection(host, username, password, database_name):
    conn = pymysql.connect(
        host=host,  # host is the IP or the URL to the server
        user=username,
        password=password,
        database=database_name
    )
    return conn


conn = get_connection('localhost',
                      os.environ.get('DB_USER'),
                      os.environ.get('DB_PASSWORD'),
                      "classicmodels")

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = """
    select `firstName`,`lastName`,`city` from
        employees JOIN offices
        ON `employees`.`officeCode` = `offices`.`officeCode`
"""

cursor.execute(sql)

for each_employee in cursor:
    print(each_employee)
