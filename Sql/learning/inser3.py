import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gaurav@2065",
    database="gauravs"
)
my_cursor = db.cursor()
sql = "INSERT INTO customer (name,address)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

my_cursor.executemany(sql, val)

db.commit()

