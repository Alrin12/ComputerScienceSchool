import pickle

f = open("pickletest.bin", "wb")

data = { 1 : 'python', 2 : 'java', 3 : 'scalar'}

#딕셔너리의 형태로 파일에 저장
pickle.dump(data, f)

f.close()
