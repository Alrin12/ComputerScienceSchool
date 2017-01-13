# Fastcampus 
## Python Advanced

---
## * args

```python
# *args의 형태
# tuple의 형태로 받는다
#인덱싱이나 for문으로 접근해 변수를 받아온다.
def func1(*args):
    print(args)
    for ele in args:
        print(ele)
```

---
## ** kwargs

```python
# **kwargs의 형태
# dictionary의 형태로 받는다
def func2(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('[key : value]  >>>  {} : {}'.format(key, value))
```

---
## * args and **kwargs

```python
# *args, **kwargs를 함께 쓰는 형태
def func3(*args, **kwargs):
    print(args)
    print(kwargs)
```

---
## * args and **kwarg 예제

```python
if __name__ =='__main__':
    #func1(1, 'a', 1.4, 'I am your father')
    #func2(name = 'greg', age = 34, money = 1000.45)
    func3(1, 1.14, name = 'greg', age = 34)
    func3(1, 'a', 1.4, 'I am your father')
    func3(name = 'greg', age = 34, money = 1000.45)
```

---
## closure

```python
def outerFunc(message):
    def innerFunc():
        print(message)
    return innerFunc

if __name__ == "__main__":
    f1 = outerFunc("I am your father!")
    f2 = outerFunc("what is your name?")
```

---
## decorator 

```python
만들고 있는 함수에 기존에 있던 함수의 기능을 추가하고 싶을 때 

미리 데코레이터 함수나 클래스를 만들어두어야 함.
```


---
## decorator by function

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'
        .format(original_function.__name__))
        return original_function(*args, **kwargs) 
    return wrapper_function
    
    
@decorator_function
def display():
    print('display function ran')
    
    
if __name__ == "__main__":
display()
print(display.__name__)

```

---
## decorator by class

```python
class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'
        .format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
        
@decorator_class
def display():
    print('display function ran')
```

---
## decorator 

```python
데코레이터를 여러 개 추가할 수는 없을까?
  : 여러 가지 기능을 추가하고 싶을 때
```

---
## decorator 

```python
from functools import wraps
```

---
## decorator 

```python
#첫 번째 기능을 담음 decorator 
def checkscores(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkscores_wrapper")
        scores=args[0]
        if not scores:
            for i in range(0, 10):
                scores.append(randint(0, 100))
        return org_func(*args, **kwargs)
    return wrapper
```

---
## decorator 

```python
#두 번째 기능을 담은 decorator 
def checkaverage(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkaverage_wrapper")
        scores = args[0]
        average = args[1]
        if not average:
            sum = 0
            for score in scores:
                sum += score
            avg = sum//len(scores)
            average.append(avg)
            
        return org_func(*args, **kwargs)
    return wrapper
```

---
## decorator 

```python
#세 번째 기능을 담은 decorator 
def checkvariance(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkvariance_wrapper")
        scores = args[0]
        average = args[1]
        variance = args[2]
        if not variance:
            sum = 0
            for score in scores:
                a = score - average[0]
                sum += a**2
            vrnc = sum//len(scores)
            variance.append(vrnc)
            
        return org_func(*args, **kwargs)
    return wrapper
```

---
## decorator 

```python
@checkscores
@checkaverage
@checkvariance
def GetStandardDeviation(scores, average, variance, std_dev):
    print("GetStandardDeviation")
    res = sqrt(variance[0])
    std_dev.append(res)
```





