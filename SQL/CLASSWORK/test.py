import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

print("Connected successfully!")

conn.close()