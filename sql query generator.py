import random
from string import digits, ascii_letters

# user table----------------------------------------------------------------
f1 = open('first names.txt', 'r').readline()
f2 = open('last names.txt', 'r').readline()
fn_list = f1.split(', ')
ln_list = f2.split(', ')

for x in range(18):

    fname, lname = random.choice(fn_list) , random.choice(ln_list)
    name = fname + ' ' + lname

    domains = ['@yahoo.com','@gmail.com','@hotmail.com','@outlook.com','@microsoft.com']
    email = (fname + lname).lower() + random.choice(digits) + random.choice(domains)
    
    num = random.randint(1000000000,9200000000)
    num = '0' + str(num)
    
    pas = ''
    for i in range(15):
        pas += random.choice(ascii_letters+digits)
    
    
    query = "(NULL,'{}','{}','{}','{}')".format(name,email,num,pas)
    print(query)

# host table--------------------------------------------------------
https://testingbot.com/free-online-tools/random-address-generator#
