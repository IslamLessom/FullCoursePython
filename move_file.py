import os

sourse = "folder"
destination = "D:\\python-islam\\folder"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(sourse,destination)
        print(sourse+"was moved")
except FileNotFoundError:
    print(sourse+"was not found")