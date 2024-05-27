import mysql.connector
gd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@2065",
    database="gauravs"
)

mycursor = gd.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Gcbjdsbodau", "High9")
mycursor.execute(sql, val)

gd.commit()
