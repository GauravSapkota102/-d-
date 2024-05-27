import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gaurav@2065",
  database = "gauravs"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")