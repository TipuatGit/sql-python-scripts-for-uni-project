import mariadb
import random as r

# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
cur.execute('SELECT guestID, listingID FROM `airbnb`.`booking`')
gl = {}
for x,y in cur:
    if x not in gl.keys():
        gl.setdefault(x, [y])
    else:
        gl[x].append(y)

ln = ['villages', 'mountains', 'oceaninc views', 'tallest places', 'city places', 'nature', 'cool apartments']
final = []
u = 20
for guest in gl.keys():
    u += 1
    for l in range(r.randint(1,10)):
        listing = None
        while True:
            listing = r.randint(1,19)
            if listing not in gl[guest]: break
            else: pass

        print(f"(NULL,{guest},{listing},'{r.choice(ln)}',NULL,'www.airbnb.com/wishlist/user{u}'),")
