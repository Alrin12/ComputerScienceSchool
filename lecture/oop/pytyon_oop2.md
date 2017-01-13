# Fastcampus 
## Python OOP - Inheritance


---
## 상속

```python
상속은 언제 쓸까?

1. is-a : 가장 이상적이다.
 Notebook is a computer.

class computer:
    pass

class notebook(computer):
    pass
   
```

---
## 상속

```python
2. has-a : 거의 하지 않는다.
  요즘은 이 경우에 객체합성을 사용한다.
  
Policeman has a gun.

class Gun:
    def __init__(self, gun_kind):
        self.gunkind = gun_kind

class Policeman(Gun):
    def __init__(self, gun_kind=''):
        self.gun = Gun(gun_kind)
        if not gun_kind:
            self.gun = None
```

---
## 상속

```python
if __name__ == "__main__":
    police_with_gun = Policeman("리볼버")
    print(police_with_gun.gun.gunkind)

    police_without_gun = Policeman()
    print(police_without_gun.gun)

실행해볼까요?
```
---
## 상속 예제 : 

```python
class Person:
    1. __init__ 함수는 생성자입니다.
    즉, 초기화를 담당합니다.
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

```

---
## Person 클래스

```python
#class_person.py
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        
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
#class_person.py

만약 이 파일이 import 모듈이 아니라 메인함수일 때 실행
if __name__ == "__main__":
    p1 = Person("taehwan", 35, 5000)
    p2 = Person("greg", 21, 2000)

    p1.giveMoney(p2, 3000)

    p1.showMyInfo()
    p2.showMyInfo()
```

---
## Retailer 클래스

```python
#class_retailer.py

#우선 상속받을 Person 클래스를 임포트
from class_person import Person

상속은 말 그대로 모든 변수와 함수를 이어받는 것

Retailer 클래스는 Person 클래스가 가지는 모든 변수와 함수를 
가지게 된다.
#상속할 때는 class <class name>(상속받을 클래스):

이렇게 하면 name, age, money 등 변수와 
giveMoney(), showMyInfo() 함수를 이어받게 됩니다.

class Retailer(Person):
  
```

---
## Retailier 클래스

```python
#class_retailer.py

class Retailer(Person):
#이렇게 선언된 변수는 클래스 변수
#모든 객체가 공유합니다.
    price = 1000
    
    def __init__(self, name, age, money, product):
        Person.__init__(self, name, age, money)
        #이렇게 선언된 변수는 객체 변수
        # 생성된 객체만 가지고 있습니다.
        self.product = product

```


---
## Retailer 클래스

```python
#class_retailer.py
#sell() 함수는 Person 클래스에는 없는 함수, 즉 추가된 함수
 def Sell(self, other, how_many):
        if self.product >=how_many and
        other.money >= self.price * how_many:
            self.product -= how_many
            other.product += how_many
            
            self.money += self.price * how_many
            other.money -= self.price * how_many

```

---
## Retailer 클래스

```python
#class_retailer.py
#이 함수는 Person 클래스에 이미 있는 함수죠.
이렇게 같은 이름을 다시 정의하면 함수 오버라이딩이라고 합니다.
Person 클래스의 함수는 가려집니다.

def showMyInfo(self):
        print("My name is {name}, {age} years old, 
        and I am a retailer".format(name = self.name, 
        age = self.age))
        print("I have {0} products and 
        {1} won".format(self.product, self.money))
```


---
## Buyer 클래스

```python
#class_buyer.py
from class_person import Person

class Buyer(Person):
    def __init__(self, name, age, money, product):
        Person.__init__(self, name, age, money)
        self.product = product

```

---
## Buyer 클래스

```python
#class_buyer.py
def Buy(self, other, how_many):
        if self.money >= other.price * how_many and 
        other.product >=how_many:
            self.product += how_many
            other.product -= how_many
            
            self.money -= other.price * how_many
            other.money +=other.price * how_many

```

---
## Buyer 클래스

```python
#class_buyer.py
    def showMyInfo(self):
        print("My name is {0}, {1} years old, 
        and I am a buyer".format(self.name, self.age))
        print("I have {0} products, and {1}
        won".format(self.product,  self.money))

```

---
## 메인함수

```python
#class_main.py
from class_person import Person
from class_retailer import Retailer
from class_buyer import Buyer

p1 = Retailer("greg", 35, 10000, 100)
p2 = Buyer("taehwan", 21, 10000, 0)

p1.showMyInfo()
print('\n')
p2.showMyInfo()

#p1.Sell(p2, 3)
p2.Buy(p1, 3)
print('\n')

p1.showMyInfo()
print('\n')
p2.showMyInfo()
```

---
## 클래스 실습 예제

```python

Person 클래스를 다시 정의하고
이를 상속받는 Boss 클래스와 Employee 클래스를 정의
보스 클래스에 함수 GiveWork()를 정의 후,
이 함수를 통해 Employee의 변수 stress를 증가
```