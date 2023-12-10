import mariadb
import random as r


# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()

cur.execute('SELECT ratingID FROM `airbnb`.`ratings_on_guest`')

for x in cur:
    print(f'({x[0]},{r.randint(1,20)}),')
