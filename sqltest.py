import os
import base64
import mariadb

# Specify the path of the folder you want to access
folder_path = r"E:\Mohsin Files\University\Semester 2\Project - Build a Data Mart in SQL\My work\Phase 2\images"

# Get a list of all files in the specified folder
##images_list = []
##for root, dirs, files in os.walk(folder_path):
##        for file in files:
##                file_path = os.path.join(root, file)
##                images_list.append(file_path)


# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()

# for each image, convert to blob and add to table in db
#for img in images_list:
img = r"E:\Mohsin Files\University\Semester 2\Project - Build a Data Mart in SQL\My work\Phase 2\images\nik-guiney-asQmJZWmfgM-unsplash.jpg"
with open(img, "rb") as image:
        b = base64.b64encode(image.read())


try:
    cur.execute("INSERT INTO `images2` VALUES (?,?,?,?,?)", (2,None,b,'unsplash.com',img))
except:
    raise
#cur.execute('UPDATE TABLE `images2` 
