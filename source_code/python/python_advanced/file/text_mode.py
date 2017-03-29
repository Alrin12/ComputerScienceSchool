
#text file 생성
'''
text_lines = ["I am your father\n",\
              "what is your name? \n",\
              "what do you want from me?\n"]

with open("test.txt", "w") as f:
    f.writelines(text_lines)
'''

#text 모드 읽기
f = open("test.txt", "r")

line = f.readline()
while line:
    length = len(line)-1
    line = line[:length]
    print(line)
    line = f.readline()
    
f.close()
