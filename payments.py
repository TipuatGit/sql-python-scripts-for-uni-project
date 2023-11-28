import mariadb
import random as r
import datetime as dt

# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
# get data from booking table
cur.execute('SELECT bookingID, guestID, booking_date, total_price FROM booking')

# store data in dict of lists
booking = {'bid':[], 'gid':[], 'bd':[], 'tp':[]}
for bid, gid, bd, tp in cur:
    booking['bid'].append(bid)
    booking['gid'].append(gid)
    booking['bd'].append(bd)
    booking['tp'].append(tp)

# get data from currency
# leaving bitcoin n digital currency out
cur.execute('SELECT currencyID, exchange_rate FROM currency WHERE exchange_rate > 0.2')
currency = {'cid':[], 'rate':[]}
for cid, rate in cur:
    currency['cid'].append(cid)
    currency['rate'].append(rate)


service = [1,2,3,4,5]
serv_amt = [1.5, 3.45, 10.89, 23.75, 50.25]
paymethod = ['Credit Card', 'Debit Card', 'Google Pay', 'Apple Pay', 'Paypal', "Bank Account", "Alipay", "Sofort Überweisung"]

for x in range(len(booking['bd'])):
    gid = booking['gid'][x]
    ser = r.choice(service)
    cid = currency['cid'][x]
    bid = booking['bid'][x]
    date = dt.datetime.combine(booking['bd'][x], dt.time.min) + dt.timedelta(hours=r.randint(1,24), minutes=r.randint(1,60), seconds=r.randint(1,60))
    pay = r.choices(paymethod, [10,10,4,4,10,3,4,2])[0]
    amt = (float(booking['tp'][x]) + r.choice(serv_amt)) * float(currency['rate'][x])
    print(f"(NULL,{gid},NULL,{ser},{cid},{bid},'{date}','{pay}',{amt:.2f}),")
