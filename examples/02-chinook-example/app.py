# import pymysql so that we can connect to MySQL
import pymysql
import os
# import dotenv so that we open our env files
from dotenv import load_dotenv
load_dotenv()


# actually access the database
conn = pymysql.connect(host='localhost',
                       user=os.environ.get('DB_USER'),
                       password=os.environ.get('DB_PASSWORD'),
                       database="Chinook")

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = """
select * from Album
join Artist on Album.ArtistId = Artist.ArtistId
limit 10
"""

cursor.execute(sql)

for each_result in cursor:
    print("Album:", each_result["Title"])
    print("Artist:", each_result["Name"])
