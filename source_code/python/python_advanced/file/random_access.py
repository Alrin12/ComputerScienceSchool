import os

with open("random_test.txt", "rb") as f:
    f.seek(2, os.SEEK_SET)
    print(f.readline()[:-1].decode())
    f.seek(-3, os.SEEK_END)
    print(f.readline()[:-1].decode())
    
