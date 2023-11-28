import json

with open("E:\Mohsin Files\Python\currency_data.txt", 'r') as f:
    currency_data = f.readlines() # creates a python list that contains string

#get string from index 0 in list and convert using json
data = json.loads(currency_data[0])

#get dict of currency codes
codes = {}
with open("E:\Mohsin Files\Python\currency_codes.txt", 'r') as f:
    for x in f.readlines():
        codes.setdefault(x.split('\t')[0], x.split('\t')[1].rstrip())

c = 1
for code in data['data'].keys():
    c +=1
    if not codes.get(code) == None:
        print(f"UPDATE `airbnb`.`currency` SET `exchange_rate` = {data['data'][code]['value']} WHERE symbol = '{code}';")
