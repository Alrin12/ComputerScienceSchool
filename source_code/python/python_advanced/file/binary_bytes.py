#test 파일 생성
'''
lines = ["abcde\n",\
         "fghij\n", \
         "klmno\n"] 
with open("random_test.txt", "wb") as f:
    for line in lines:
        f.write(line.encode())
'''

read_lines = []

f = open("random_test.txt", "rb")

line = f.readline()

while line:
    length = len(line)-1
    line = line[:length]
    read_lines.append(line.decode())
    line = f.readline()

for line in read_lines:
    print(line)

f.close()
    
