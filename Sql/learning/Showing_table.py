import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gaurav@2065",
  database = "gauravs"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES0")

for x in mycursor:
  print(x)