import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@2065",
    database ="gauravs"
)
mycursor = db.cursor()
mycursor.execute("")