f = open("test.txt", "r")


'''
while 1:
    data = f.readline()
    if not data:
        break
    strlen = len(data)-1
    _data = data[0:strlen]
    print(_data)
'''


'''
data = f.readlines()
#print(data)
for s in data:
    print(s, end='')
'''

data = f.read()
print(data)

for i in data:
    print(i)

f.close()
