import random as r

taxes = [
    "Transient Occupancy Tax",
    "Tourist Development Tax",
    "Municipal Hotel Tax",
    "City Lodging Fee",
    "Occupancy Assessment Tax",
    "Accommodation Tax",
    "Lodging Tax",
    "Resort Tax",
    "Tourism Improvement District Assessment",
    "Hospitality Tax",
    "Room Surcharge",
    "Tourism Promotion Fee",
    "Guest Room Assessment",
    "City Sales Tax",
    "Local Tourism Levy",
    "Destination Marketing Fee",
    "Tourism Infrastructure Fee",
    "Hotel Occupancy Fee",
    "Bed Tax",
    "Local Government Assessment"
]

for x in range(20):
    print(f'(NULL, NULL, {r.randint(1,17)+ int(x)*0.2}, "{taxes[x]}"),')
