import datetime
from random import randint, choice, choices
import mariadb


# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()

query = 'SELECT listingID, available_from, available_until FROM `airbnb`.`availability`'
cur.execute(query)

availability = {'id':[],'af':[],'au':[]}
for id,af,au in cur:
    availability['id'].append(id)
    availability['af'].append(af)
    availability['au'].append(au)

# guestid : 2-21
# listingid: 1-20
# bookingid: serial sequence
# booking_per_guest: 1-5
all_queries = []
bookingid = 0
    
for guestid in range(2,18):
    bf = None
    bu = None
    times_guest_books = randint(1,6)
    guest_num = randint(1,7)
    for booking in range(1,times_guest_books):
        bookingid += 1
        listingid = randint(0,19)
        af= availability['af'][listingid]
        au= availability['au'][listingid]
        booking_date = af - datetime.timedelta(days = randint(7,33))
        bf = au + datetime.timedelta(days=1)
        bu = bf + datetime.timedelta(days = choice([7,15,20,30,45]))
        availability['af'][listingid] = bu
        availability['af'][listingid] = bu + datetime.timedelta(days=1)
        if listingid == 0:
            listingid = 1

        ci = datetime.datetime.combine(bf, datetime.time.min)
        ci += datetime.timedelta(hours=randint(1,24), minutes=randint(1,60), seconds=randint(1,60))
        co = datetime.datetime.combine(bu, datetime.time.min)
        co += datetime.timedelta(hours=randint(1,24), minutes=randint(1,60), seconds=randint(1,60))

        total_price = ((bu-bf).days) * randint(50,200)
        stat = choices(population=['rented','booked','missed','cancelled'], weights=[8,5,1,1],k= 1)[0]
        query=f"({bookingid},{guestid},{listingid},'{booking_date}','{bf}','{bu}','{ci}','{co}',{total_price},{guest_num},'{stat}'),"
        all_queries.append(query)

for x in all_queries:
    print(x)

    
