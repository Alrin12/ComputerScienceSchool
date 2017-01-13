# Fastcampus 
## Python Basic

---
## 파일 입출력

```python
f = open("test.txt", "w") : 파일을 열 때

f.close() : 파일을 닫을 때
```

---
## 파일 입출력

```python
입출력 모드의 결정
1. 'write text' 모드
f = open("test.txt", "wt")

2. 'write binary' 모드
f = open("test.bin", "wb")

3. 'read text' 모드
f = open("test.txt", "rt")

4. 'read binary' 모드
ㄹ = open("test.bin", "rb")
```

---
## 파일 입출력

```python
1. 파일에 쓰기
f.write(data) : 데이터를 파일에 출력

2. 파일에서 읽기
 1) f.readline() 
    : 파일에서 한줄 단위로 읽어들일 때
 
 2) f.readlines() 
    : 모든 라인을 읽어서 리스트로
 
 3) f.read() 
    : 문자열로 한방에!
```

---
## 파일 입출력

```python
import pickle

1. 파일에 자료형 그대로 쓰기
data = { 1 : 'python', 2 : 'java'}
pickle.dump(data, f)

2. 파일에서 자료형 그대로 읽기
data = pickle.load(f)
```

---
## 파일 입출력 실습

```python
주어진 성적 데이터를 파일에서 불러와 
반 평균과 분산을 구하는 예제
파일에 저장된 데이터 형식
{'name' : '양태환' , 'score' : 95}
```

---
## 모듈

```python
미리 만들어 둔 python 파일 == 모듈
함수나 클래스를 불러와 사용
```

---
## 모듈

```python
#calc.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a//b

```

---
## 모듈

```python
#main.py

import calc # 모듈을 불러오는 방법 1

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

함수 접근 방법 1 : <모듈>.<함수이름>

print("a + b = {}".format(calc.add(a, b)))
print("a - b = {}".format(calc.subtract(a, b)))
print("a * b = {}".format(calc.multiply(a, b)))
print("a // b = {}".format(calc.divide(a, b)))
```

---
## 모듈

```python
#main.py

from calc import * # 모듈을 불러오는 방법 2

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

함수 접근 방법 2 : <함수이름>

print("a + b = {}".format(add(a, b)))
print("a - b = {}".format(subtract(a, b)))
print("a * b = {}".format(multiply(a, b)))
print("a // b = {}".format(divide(a, b)))
```



---
## os 모듈

```python
import os

print(dir(os)) : 모든 attributes, methods를 보여준다.

```

---
## os 모듈

```python
1. get current working directory
os.getcwd()

2. change directory
os.chdir()

3. list directory
os.listdir()

4. make directory
os.mkdir('testfolder')

5. remove directory
os.rmdir('testfolder')
```

---
## os 모듈

```python
6. rename a file or a directory
os.rename('test.txt', 'pypy.txt')
os.rename('testfolder', 'pypyfolder')

7.statistics for a file or a directory
os.stat('pypy.txt')
os.stat('pypy.txt').st_size : 파일 사이즈를 바이트 단위로

8. walk all of directory trees
os.walk('C:\\Users\\user\\desktop')
```

---
## os 모듈

```python
9. 환경변수(environment variable) 접근
os.environ
os.environ.get('HOME') : 환경변수에 등록되어 있는 홈 디렉토리

10. file path manipulation
fpath = 
   os.path.join(os.environ.get('HOME'), 'desktop/text.txt')
print(fpath)

with open(fpath, 'w') as f:
	f.write("python is good. We can do everything!")
```



