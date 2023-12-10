import mariadb
import random as r


# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()

cur.execute('SELECT guestID, listingID FROM `airbnb`.`booking`')
a,b = [],[]
c = 0
for x,y in cur:
    c += 1
    a.append(f'(NULL,{x},{r.choices([4,5],[2,10])[0]}),')
    b. append(f'({c},{y}),')

for x in a:
    print(x)

print()

for x in b:
    print(x)
