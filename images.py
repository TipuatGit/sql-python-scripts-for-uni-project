import os

p = os.walk(r'E:\Mohsin Files\University\Semester 2\Project - Build a Data Mart in SQL\My work\Phase 2\images')

a = None
loc = None
filenames = None
for x in p:
    a = x
loc = a[0]
filenames = a[2]

for x in filenames:
    s = x.replace("-unsplash.jpg", '')
    #print("(NULL, HEX("+str(loc)+str(x)+"), 'www.unsplash.com/"+s+ ", 'E:\\images\\"+x+"'),")
    print(f"(NULL, HEX('{loc+x}'),'www.unsplash.com/{s}', 'E:\\images\\{x}'),")
