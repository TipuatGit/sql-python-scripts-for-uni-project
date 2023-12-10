import random as r
import datetime as dt
import mariadb
socials = ['facebook', 'twitter', 'instagram', 'whatsapp', 'snapchat', 'telegram', 'tumblr', 'twitch', 'kik',  'linkedin', 'line', 'Weibo', 'wechat', 'tiktok']
com = '.com'


# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
cur.execute('SELECT name FROM `airbnb`.`user`')

n = []
for x in cur:
    n.append(x[0])

for x in range(40):
    rating = r.choices([1,0],[9,1])[0]
    dc = dt.datetime(year=2023, month=r.randint(9,11), day=r.randint(1,30), hour=r.randint(0,23), minute=r.randint(0,59), second=r.randint(0,59))

    name = r.choice(n).strip().replace(' ', '').replace('.','').lower()
    for social in range(r.randint(2,6)):
        s = r.choice(socials) + com + '/' + name
            
        print(f"(NULL,{x+1},'www.{s}',{rating},'{dc}', NULL),")
