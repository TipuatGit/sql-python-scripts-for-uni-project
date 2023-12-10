import random as r

#listing from 1-20
#images from 54-123

for l in range(20):
    for i in range(r.randint(3,5)):
        print(f'({l+1}, {r.randint(54,123)}),')
