import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MohamedBoussetta2001@Dakhla"
)

cursor = mydb.cursor()
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"failed to conect to DB : {err}")

cursor.close()
mydb.close()

