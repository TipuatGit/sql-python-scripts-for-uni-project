import mariadb
import random as r
import datetime as dt
from string import ascii_uppercase, digits

# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
# get data from booking table
cur.execute('SELECT bookingID, booking_date FROM booking WHERE status IN (?, ?)', ('booked', 'rented',))

bid = []
bd = []
for x,y in cur:
    bid.append(x)
    bd.append(y)

#date = f'{} {r.randint(1,24)}:{r.randint(0,60)}:00'
for x in range(len(bd)):
    code=''
    for a in range(4):
        code += r.choice(ascii_uppercase)
    for b in range(4):
        code += r.choice(digits)

    disc = r.choices([20,30,50,100,120], [5,8,4,2,1])

    cd = bd[x] + dt.timedelta(hours = r.randint(1,6))
    ed = cd + dt.timedelta(days = 1)
    print(f"(NULL, {bid[x]}, '{code}', {disc[0]}, '{cd}', '{ed}'),")
