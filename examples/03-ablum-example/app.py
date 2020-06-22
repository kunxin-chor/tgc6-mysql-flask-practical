import pymysql
import os
from dotenv import load_dotenv

# 1. LOAD IN THE ENVIRONMENT VARIABLES
load_dotenv()

# 2. CREATE THE DATABASE CONNECTION
conn = pymysql.connect(host="localhost",
                       user=os.environ.get("DB_USER"),
                       password=os.environ.get("DB_PASSWORD"),
                       database="Chinook"
                       )

# 3. CREATE THE CURSOR
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 4. DEFINE THE SQL STAEMENT

track_name = input("Please enter a track name: ")

sql = f"""
select * from Track where Name like "%{track_name}%"
limit 10 
""" 

print(sql)

# 5. EXECUTE THE STATEMENT
cursor.execute(sql)

# 6. OUTPUT THE RESULTS
for each_result in cursor:
    print("Track:", each_result['Name'])
    print("Composed by:", each_result['Composer'])
    print()

# rewind cursor if we want to go through the results again
# cursor.scroll(0, 'absolute')

# for each_result in cursor:
#     print("Track:", each_result['Name'])
#     print("Composed by:", each_result['Composer'])
#     print()