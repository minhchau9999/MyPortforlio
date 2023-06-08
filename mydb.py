import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd ='pwd123'
)

#prepare a cursor object
cursorObject = db.cursor()

#create db

cursorObject.execute("CREATE DATABASE portfolio")

print("db created")