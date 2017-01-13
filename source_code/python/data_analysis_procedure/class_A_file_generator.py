import pickle

f = open("class_A.bin", "wb")

data = {'greg' : 95}
pickle.dump(data, f)

data = {'john' : 25}
pickle.dump(data, f)

data = {'yang' : 50}
pickle.dump(data, f)

data = {'timothy' : 15}
pickle.dump(data, f)

data = {'melisa' : 100}
pickle.dump(data, f)

data = {'thor' : 0}
pickle.dump(data, f)

data = {'elen' : 25}
pickle.dump(data, f)

data = {'mark' : 80}
pickle.dump(data, f)

data = {'steve' : 95}
pickle.dump(data, f)

data = {'anna' : 10}
pickle.dump(data, f)


f.close()
