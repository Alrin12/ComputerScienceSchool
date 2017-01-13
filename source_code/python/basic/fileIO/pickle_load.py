import pickle

f = open("pickletest.bin", "rb")

data = pickle.load(f)

print(data)

f.close()
