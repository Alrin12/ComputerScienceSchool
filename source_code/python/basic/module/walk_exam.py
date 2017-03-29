import os

for dirpath, dirnames, filenames in os.walk("C:\\Users\\User\\Desktop\\start"):
    print("current path : {}".format(dirpath))
    print("directories : {}".format(dirnames))

