import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@2065"
)

# my_cursor = db.cursor()

my_cursor = mydb.cursor()


my_cursor.execute("SHOW DATABASES")
for i in my_cursor:
    print(i)