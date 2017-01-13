f = open("test.txt", "w")

for i in range(1, 4):
    data = input("문자열을 입력하세요 : ")
    data += '\n'
    f.write(data);

f.close()

