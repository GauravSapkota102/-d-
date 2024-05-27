import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@2065",
)

my_cursor = db.cursor()
my_cursor.execute("CREATE DATABASE gauravs")

