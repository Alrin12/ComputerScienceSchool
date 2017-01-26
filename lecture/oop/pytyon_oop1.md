# Fastcampus 
## Python OOP

---
## 클래스

```python
class <클래스 이름>(상속받을 클래스):
	<class 변수>
    
    def __init__(self, arg1, arg2, ...):
    	self.arg1 = arg1
        self.arg2 = arg2
        ...
    
    def <클래스 함수 이름>(self, arg, ...):
        <실행문1>
        <실행문2>
        ....

```

---
## 클래스

```python
객체와 인스턴스의 차이
 : 둘 모두 같은 것을 가리킵니다.
 
   인스턴스는 클래스 입장에서 생성된 클래스를 가리킬 때
   ex)  
   greg = Person('greg', 34)
   greg은 메모리에 올라와 있는 오브젝트
   즉, "greg은 객체이다"
   
   클래스의 입장에서는
   "greg은 Person 클래스의 인스턴스다"
```

---
## 클래스

```python
클래스 변수와 객체변수

class Person:
    #클래스 변수 : 모든 객체가 공유한다
    planet = 'Earth'
    
    def __init__(self, name, age, money):
    	#객체변수 초기화
        self.name = name
        self.age = age
        self.money = money
```

---
## 클래스

```python
객체 함수 
def giveMoney(self, other,how_much):
        if how_much <=self.money:
            other.money +=how_much
            self.money -= how_much
        else:
            print("you don't have {0}".format(how_much))

    def showMyInfo(self):
        print("{0} has {1}".format(self.name, self.money))
```

---
## 클래스

```python
클래스 함수
 # class method : 첫번째 매개변수로 class를 자동으로 받는다.
    # 주로 생성자 오버로딩으로 쓰인다.(파이썬에서는 원칙적으로 생성자 오버로딩 안됨)
    @classmethod
    def FromString(cls, string):
        name, age_int, money_int = string.split('-')
        age = int(age_int)
        money = int(money_int)
        return cls(name, age, money)

    #클래스 변수의 값을 변경할 때 사용한다.
    @classmethod
    def ChangePlanet(cls, pln):
        cls.planet = pln
```

---
## 클래스

```python
static 함수
 #static method : 전역변수처럼 쓸 수 있다.
    # 클래스와 관련있을 경우 클래스 내에 선언(캡슐화)
    @staticmethod
    def SavingCalculator(amount_per_month, months):
        return amount_per_month * months

    #객체함수에서도 static 함수를 불러와 쓸 수 있다.
    def PredictMoney(self, apm, mons):
        return self.money + Person.SavingCalculator(apm, mons)
```

---
## OOP 주요 개념

```python
1. 캡슐화
  : 클래스를 관련 있는 변수(attribute)와 
    관련 있는 함수(method)로 잘 묶어주는 것이 관건
    
    이를 캡슐화라고 한다.
    
    즉, 어디까지 묶을 것인가 
        어디부터 다른 클래스로 만들 것인가?
```

---
## OOP 주요 개념

```python
2. 정보은닉
파이썬은 정보은닉을 지원하지 않습니다.......


```

---
## 절차지향에서 객체지향으로... 

```python
1. 평균, 분산, 평가만을 담당하는 연산클래스 정의
    Evaluate 클래스
    
2. 파일에서 가져온 데이터를 직접 가지고 있고 평균, 분산, 
   표준편차 데이터도 가지고 있는 데이터 핸들러 클래스 정의
   DataHandler 클래스
   
3. 메인함수 정의
```

---
## 절차지향에서 객체지향으로... 

```python
# EvaluateClass.py
# 평균 등을 구하는 기능만을 담당
class Evaluate:
	def average(self, scores):
	def variance(self, scores, avrg):
	def evaluateClass(self, avrg, std_dev):
```

---
## 절차지향에서 객체지향으로... 

```python
# DataHandlerClass.py
#모든 데이터를 다룬다.
class DataHandler:
	def GetScores(scores, items):
	def __init__(self, filename, clsname):
	def GetAverage(self):
	def GetVariance(self):
	def GetStandardDeviation(self):
	def GetEvaluation(self):
```

---
## 절차지향에서 객체지향으로... 

```python
#oop_data_answer.py
from DataHandlerClass import *

dh = DataHandler('class_A.bin', 'A')
dh.GetEvaluation()
```


