# Fastcampus 
## Python Basic


---
## Python Basic

### Python은? 
1989년 크리스마스 연휴를 보내던  Guido van Rossum이 만든 고급 프로그래밍 언어

### 특징
- 인터프리터
- 객체지향
- 동적타이핑
- 엄격한 문법

---
## Python Basic

Python으로 할 수 있는 것들!
- System Programming
- Web Programming
- Data Analysis
- ...

---
## Python Basic

### REPL - Read - Eval - Print Loop
코드를 입력하면 바로 결과를 확인할 수 있음!!

### We'll use python3

[difference of 2.x , 3.x](https://wiki.python.org/moin/Python2orPython3)
Short version: Python 2.x is legacy, Python 3.x is the present and future of the language

---
## Hello python!

파이썬의 철학

```python
>>>import this
```

---
## Hello python!

So, let's try!!

```python
print("hello python!")
```

---
## Before learning python!

Call by value??  Call by referenace??
Neither!!

```python
>>>li = [1, 2]
>>>def func(a):
        a.append(3)
    	a = [11, 12]
    
>>>func(li)
>>>print(li)
[1, 2, 3] ?!?!?!
```

---
## Numbers

```python
>>>a = 10    정수형 
>>>b = 1.56  실수형
```

---
## Numbers......메모리 참조 원리!

```python
>>>a = 10     
>>>b = 10
>>>id(a)
1661819296
>>>id(b)
1661819296
>>>a = 15
>>>print(id(a), id(b))
1661819376 1661819296 ......?!?!
```

---
## Numbers & Math

```python
print(3 + 7)
print(10 - 3)
print(15 / 7) 	: 실수형 나누기
print(15//7) : 정수형 나누기
print(34 * 100)
```

---
## Boolean

```python
print(3 < 7)
print(10 < 3)
print(15 > 7)
print(34 == 100)

!=
>=
<=
```

---
## Variable

```python
print("hello python!")
hello = "hello"
python = "python!"
print(hello, python)
print(hello + python)
```
```python
num1 = 14
num2 = 5

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
```

---
## input
```python
name = input("What is your name? ")
print("Hi, ", name)
```

## input with evaluation
```python
eval('수식')
>>>eval('10 + 20')
>>>eval(input("수식을 입력하시죠 : "))
수식을 입력하시죠'i am your' + ' father!'
'i am your father!'
```

---
## String : 변경 불가능

```
a = "I am your father!" or a = ' i am your father!'
```

```
1. 문자열 더하기
>>>a = "python" + " is easy"
>>>print(a)
 
2. 문자열 곱하기
a = "="
print(a * 50)
```

---
## String Formatting

```
print("I have a %s, I have an %s." % ("pen","apple"))
```

```
%s - string
%c - character
%d - Integer(decimal)
%f - floating-point
%o - 8진수(Octal)
%x - 16진수(hexadecimal)
%% - %
```

---
## String Functions
```
s = "Python is, easy to learn, however powerful"

1. 문자 개수 세기 
s.count('p') : 문자열 안에 'p'가 몇 개?

2. 문자 위치 찾기 
s.find('p') : 'p'가 처음 나오는 인덱스 반환

3. 문자열 insert
s2 = ','.join('python') :','를 인서트 하여 문자열 생성

4. 문자열 나누기
s.split(',') : ','를 기준
s.split() : 공백 기준

5. 부분 문자열 대체 
s.replace("python", "C++")
```


---
## List, Tuple, Dictionary
List : 변경 가능
```
animals = ['lion','hippo','cat']
```

Tuple : 변경 불가능

```
animals = ('lion','hippo','cat')
```
Dictionary : 변경 가능
```
user = {'name':'fastcampus','age':'27',
city:['seoul','busan','incheon']}
```

---
## List detail
```
list_nam	e = [요소1, 요소2, 요소3, ....]

a = [1, 2, 'a', 'b', [4, 5, 6]] : 같은 자료형이 아니어도 됨

1. 인덱싱
>>> a[1]
2
>>> a[4][-1]
6
```
---
## List detail
```
a = [1, 2, 'a', 'b', [4, 5, 6]]

2. 슬라이싱
>>> a[0:3] : 0이상 3 미만 (3은 포함되지 않음!!)
1, 2, 'a'
```
---
## List detail
```
a = [1, 2, 'a', 'b', [4, 5, 6]]

3. del
>>> del a[1]
[1, 'a', 'b', [4, 5, 6]]

4. append
>>>a.append(4)
[1, 'a', 'b', [4, 5, 6], 4]

5. insert
>>>a.insert(1, 2)
[1, 2, 'a','b',[4, 5, 6], 4]

```
---
## List detail
```
a = [1, 2, 'a', 'b', [4, 5, 6], 4]

6. remove
>>> a.remove('a')
[1, 2, 'b', [4, 5, 6], 4]

7. pop
>>>a.pop()
4
>>>a
[1, 2, 'b', [4, 5, 6]]

8. sort
>>> b = [ 3, 2, 1, 4]
>>> b.sort()
[1, 2, 3, 4]
```

---
## List : 메모리 참조 원리!
```
>>>a = [1, 2, 3]
>>>b = a
>>>print(id(a), id(b))
65960216 65960216
>>>b[1] = 4
>>>b
[1, 4, 3]
>>>a
[1, 4, 3].....?!?! 너는 왜 바뀌었니??
>>>print(id(a), id(b))
65960216 65960216
```

---
## If
```python
if 조건:
	실행문

if 조건1 and 조건2:
	실행문

if 조건1 or 조건2:
	실행문
if not 조건:
	실행문
```

### Comparison Operators
```
x == n
x != n

x < n
x > n
x <= n
x >= n
```

---
## else
```python
if 조건:
	실행문1
else:
	실행문2
```

## else if

```python
if 조건1:
	실행문1
else:
	if 조건2:
		실행문2
	else:
		실행문3
```

---
## elif
```python
if 조건1:
	실행문1
elif 조건2:
	실행문2
elif 조건3:
	실행문3
...
else:
	실행문n
```

---
## numguess
```python
import random


answer = random.randint(1,100)
print(answer)
```

---
## numguess
```python
username = input("Hi there, What's your name?? ")
guess = eval(input("Hi, "+ username + "guess the number: "))

if guess == answer:
	print("Correct! The answer was ", str(answer))
else:
	print("That's not what I wanted!! The answer was ",
    str(answer))
```

---
## numguess advanced!!

how to make it look like a real game??

1. 반복문
2. 재귀호출

---
## For, while
```python
for 변수 in (리스트 or 문자열):
	실행문1
    ...
```
```python
for i in ["python", "java", "golang"]:
	print(i)
```

---
## For, while
```python
sum = 0
for i in range(1,11):
	sum += i
	print(sum)
```
### List Comprehension
```python
result = [i for i in range(1,11)]
print(result)
```

---
## For, while
```python
while 조건:
	실행문1
	...
```

```python
while name != "foo bar":
	name = input("What's your name? ")
	print("Hi, " + name + "So, where is foo bar?")
```

```python
while 1:
	print("Hello world!")
```


---
## Fizzbuzz

```python
num = eval(input("type the number: "))

for i in range(1, num):
	if i % 15 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("fizz")
	else:
		print(i)
```

---
## Refactoring numguess
```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
	guess = eval(input("Hi, "+ username + "guess the 
    number: "))

	if guess == answer:
		print("Correct! The answer was ", 
        str(answer))
		break
	else:
		print("That's not what I wanted!! 
        Try again!!")
```

---
## function
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Function_color_example_3.svg/440px-Function_color_example_3.svg.png)
- 수학적 정의: 첫 번째 집합의 임의의 한 원소를 두 번째 집합의 오직 한 원소에 대응시키는 대응 관계
- x: 정의역 y: 공역

---
## function
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/440px-Function_machine2.svg.png)
- 프로그래밍에서의 함수: 입력값을 내부에서 어떤 처리를 통해 결과값을 출력하는 것

---
## function

```python
def function(parameter):
	실행문1
	실행문2
	...
```

---
## Leap year
4로 나뉘어 떨어지면 윤년,
100으로 나뉘어 떨어지면 평년,
400으로 나뉘어 떨어질땐 윤년

---
## Leap year(answer)
```python

def is_leap(y):
	leap = False
	if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
		leap = True
	return leap
    
y = int(input("Is leap?? "))
print(is_leap(y))

```

---
## numguess with function

```python
def guesser(guess):
	if guess == answer:
		print("Correct! The answer was ", str(answer))
		break
	else:
		print("That's not what I wanted!! Try again!!")
```

