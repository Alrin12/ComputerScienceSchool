import sys
import pickle

class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "a is {} and b is {}".format(self.a, self.b)
'''
b1 = Base(1, 2)
b2 = Base(3, 4)

with open("test.bin", "wb") as f:
    pickle.dump(b1,f)
    pickle.dump(b2, f)
'''

li = []

f = open("test.bin", "rb")

try:
    while 1:
        li.append(pickle.load(f))
except EOFError as e:
    print(e)

for baseObj in li:
    print(baseObj)

f.close()





