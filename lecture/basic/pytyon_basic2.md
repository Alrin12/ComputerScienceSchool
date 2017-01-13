# Fastcampus 
## Python Basic

---
## dictionary
```python
dic1 = {key1 : value1, key2 : value2, key3 : value3, .....}

1. key 값은 고유! 중복 안됨!
dic1 = { 'name' : "양태환" , 'name' : "강동원",  "age" : 35,
"weight" : 70.5}라고 하면....

key 값 중 하나는 무시

2. key를 이용해 value를 얻는 첫 번째 방법
>>>>>>dic1['name']
"양태환"
```

---
## dictionary
```python
dic1 = { 'name' : "양태환" , "age" : 35, "weight" : 70.5}

3. key - value 추가
>>>dic1['money'] = 5000
>>>dic1
value에는 리스트도 들어갈 수 있다.
dic1['lang'] =['python', 'C', 'C++', 'C#']
>>>dic1

중요! 
딕셔너리에는 순서가 없다!! 리스트는 순서 있음
>>>dic1['lang'][2]
```

---
## dictionary
```python
dic1 = { 'name' : "양태환" , "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

4. del을 이용한 삭제
>>>del dic1['name']
>>>dic1

5. value에 접근은 key 값으로... 리스트는 인덱싱으로 했었죠!
```

---
## dictionary
```python
dic1 = { "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

6. key만 따로 뽑고 싶을 때
>>>dic1.keys() 
dict_keys(['money', 'age', 'weight'])

주의사항!
우리가 알던 리스트는 아닙니다. 리스트처럼 사용하려면...
>>>li = list(dic1.keys())
>>>li
['money', 'age', 'weight']
```

---
## dictionary
```python
dic1 = { "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

7. value만 따로 뽑고 싶을 때
>>>dic1.values()
key와 마찬가지로 리스트로 사용하고 싶다면!
>>>li2 = list(dic1.values())

```

---
## dictionary
```python
dic1 = { "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

8. key-value 쌍을 뽑고 싶을 때
>>>dic1.items()
key 와 value 값을 튜플로 묶어서 내보내줍니다!
리스트로 이용하고 싶다면?
>>>li3 = list(dic1.items())
```

---
## dictionary
```python
dic1 = { "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

9. key로  value를 얻는 두 번째 방법
>>>dic1.get("age")

dic1['age'] VS. dic1.get('age')
없는 키를 넣을 경우
>>dic1['sdf'] 
: KEY ERROR!!
>>dic1.get('sdf']
None을 반환, 에러는 아니다!

 결론 : 상황에 따라 다른 방법으로 구현해야 함.
```

---
## dictionary
```python
dic1 = { "age" : 35, "weight" : 70.5, 
'money' : 5000, 'lang' : ['python', 'C', 'C++', 'C#']}

dic1['age'] VS. dic1.get('age')
예제:
 없는 키가 생성될 가능성이 있으나 그 상황만 제외하면 
 계속해서 프로그램을 진행해야 하는 상황일 때
 
k = input("key 값을 입력하세요 : ") 
if not dic1.get(k):
	print("없는 키 값이지만 봐줍니다!")
else:
	print(dic1.get(k))
```

---
## set 
```python
>>>s = set([1, 2, 3, 4])
>>>s
{1, 2, 3, 4}

1. set : 집합을 표현하기 위한 자료형

2. unordered, 즉 순서가 없다! 
   - 순서가 있는 것 : list, tuple
   - 순서가 없는 것 : dictionary, set
```

---
## set 
```python
s = set([1, 2, 3, 4])

3. add() : 한 개 추가
>>>s.add(5) 
>>>s
{1, 2, 3, 4, 5}

4. update() : 여러 개 추가
>>>s.add([6, 7, 8])
>>>s
{1, 2, 3, 4, 5, 6, 7, 8}

5. remove() : 한 개 제거
>>s.remove(5)
>>>s
>>>{1, 2, 3, 4, 6, 7, 8}
```

---
## set 
```python
s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

6. & or intersection() : 교집합
>>>s1 & s2
{3, 4}
>>>s1.intersection(s2)

7. | or union() : 합집합
>>>s1 | s2
{1, 2, 3, 4, 5, 6}
>>>s1.union(s2)

8. - or difference() : 차집합
>>>s1 - s2
{1, 2}
>>>s1.difference(s2)
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

반복문

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
## function : 변수의 유효 범위  when immutable
```python
변경 불가능 변수, 즉, 정수 상수, 문자열, 튜플 등

함수를 벗어나면 유효하지 않다(call by value)

```

---
## function : 변수의 유효 범위  when immutable
```python
a = 10
b = 5

def func(a, b):
    print("a = {0}, b = {1}  before change in func".format(a, b)) 
    a, b = b, a
    print("a = {0}, b = {1}  after change in func".format(a, b)) 

print("a = {0}, b = {1} before".format(a, b))
print("\n")
func(a, b)
print("\n")
print("a = {0}, b = {1} after".format(a, b))

```


---
## function : 변수의 유효 범위 when mutable
```python
변경가능 변수, 즉 list, dictionary 등에서

1. 함수 내에서 기존 list를 수정만 하는 경우
함수를 벗어나도 계속 유효(즉, call by reference)

2. 함수 내에서 새로운 list를 참조하는 경우
함수를 벗어나면 유효하지 않다(즉, call by value)

```

---
## function : 변수의 유효 범위 when mutable
```python
# 기존 list를 변경만 한다
def func(li):
    print("first li in func1 li = ", id(li))
    li[2] = 15
    li.remove(2)
    del li[0]
    li.append([11, 12, 13])
    print("second li in func1 li = ", id(li))
```

---
## function : 변수의 유효 범위 when mutable
```python
# 함수 안에서 새로운 list를 참조
def func2(li):
    print("first li in func2 li = ", id(li))
    li = [11, 12, 13]
    print("second li in func2 li = ", id(li))
```

---
## function : 변수의 유효 범위 when mutable
```python
a = [1, 2, 3, 4]

print("before func  --> a = ", id(a))
print("\n")

func(a)
#func2(a)

print("\n")
print("after func --> a = ", id(a))

print(a)

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

---
## 파일 입출력

```python
f = open("test.txt", "w") : 입력 모드로 열 때

f.close() : 출력 모드로 닫을 때
```

---
## 파일 입출력

```python
f.write(data) : 데이터를 파일에 출력

f.readline() : 파일에서 한줄 단위로 읽어들일 때
```
