import mariadb
import random as r
import datetime as dt
from string import ascii_uppercase, digits

# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
# get data from booking table
cur.execute('SELECT listingID, guestID, check_out FROM booking WHERE status IN (?, ?)', ('booked', 'rented',))

lid = []
gid = []
cout = []
for x,y,z in cur:
    lid.append(x)
    gid.append(y)
    cout.append(z)
    
comment=['Good place.','Nice stay.','Lovely Place.','It was great! Thanks to host for hospitality.',
         'I really loved it! The scenery, the environment...superb! Definitely recommend!','Great place which was cozy and comfy.',
         'Our Family loved the visit! We recommend it to anyone!','Well maintained and clean place. Great food!',
         'The residence was bright, the night sky views were amazing.','I loved the place and the host!',
         'It was a good place, coming back again.','Thanks the host for great hospitality!',
         'Its Okay.','It was nice.','Good.','We old timers had a great time together with the host. Very hospitable. Great people.',
         'It was Alright.','Best host ever! Highly recommended!']
#date = f'{} {r.randint(1,24)}:{r.randint(0,60)}:00'
for x in range(len(gid)):
    rating = r.choice(digits)
    d = cout[x] + dt.timedelta(days=r.randint(1,3), hours=r.randint(1,24), minutes=r.randint(0,60), seconds=r.randint(0,60))
    print(f"(NULL, {lid[x]}, {gid[x]}, '{d}', '{r.choice(comment)}', {rating}),")
