import os
# closure
#inner 함수의 인터페이스, 즉 매개변수에 접근할 수 있는 방법이 없네요
#아래와 같은 기법을 통해 정보 은닉등을 구현할 수 있습니다 
#하지만 그리 자주 쓰이는 방법은 아닙니다

#이러한 기법을 이용해 구현할 수 있는 다른 예는
#유저에게서 필요한 정보만을 제공 받아 (아래 함수에서는 msg)
#특정기능은 함수의 설계자가 도맡아(아래 함수에서는 메세지를 출력하는 기능)할 수 있죠
'''
def outer(msg):
    def inner():
        print (msg)
    return inner

f = outer("abc")

#inner 함수가 반환되므로 이를 함수처럼 사용할 수 있습니다.
f()
f()
f()
f()
#실제로 함수의 이름을 출력해보면....
print(f.__name__)
'''

#decorator의 서막 - msg 대신에 함수를 대입해보자?
#아래와 같이 설계해봅시다
#실제 기능을 담당할 original function은 반드시 매개변수가 하나도 없는 형태가 되어야 하죠
'''
def outer(org_func):
    def inner():
        print("inner excuted!")
        return org_func()
    return inner

#original function
def func1():
    print("my name is func1")

var1 = outer(func1)
var1()
var1()
'''

#그런데 별로 쓸모가 없어보이네요.... 이걸 어디에다 써 먹지....?!
# 자 이제 original function에 매개변수를 넣어봅시다
#그렇게 하려면 *args를 이용하면 될 것 같군요
#closure 함수부터 바꿔보죠
'''
def outer(org_func):
    def inner(*args):
        print("inner excuted!")
        return org_func(*args)
    return inner

#original function
def func2(a, b, c):
    d = a + b + c
    print("{} + {} + {} = {} 입니다.".format(a, b, c, d))

var2 = outer(func2)
var2(1, 2, 3)
var2(4, 5, 6)
'''

# 오오 이제 좀 쓸만 하네요!
#그런데 항상 먼저 inner 함수의 print 함수의 기능이 먼저 실행되고 original function이 실행되네요
#이걸 잘 이용하면 뭔가 멋진 일을 할 수 있을 거 같은데........


# decorator의 완성 - 미리 만들어둔 기능을 지금 내가 설계하는 함수에 간단하게 추가하기!

'''
def outer(org_func):
    def inner(*args, **kwargs):
        print("추가하려는 기능 실행 시작")
        print(os.getcwd())
        print("추가하려는 기능 실행 종료")
        return org_func(*args, **kwargs)
    return inner


#original function
def func3(li):
    sum = 0
    for l in li:
        sum += l
    result = sum//len(li)
    print("리스트의 평균은 : {}".format(result))
'''


'''
#아래처럼 함수를 변수로 받아서 쓰면 됩니다.
var3 = outer(func3)
var3([4, 4, 10, 10, 12, 16])
'''

'''
#새로운 변수 대신에 func3로 받아서 쓸 수도 있습니다
func3 = outer(func3)
func3([4, 4, 10, 10, 12, 16])
func3([5, 5, 5, 5, 5])
print(func3.__name__)
'''

#위와 같은 방법
# 즉 func = outerfunction(func)을 문법으로 만들면 그것이 바로 decorator!!!


#위에 있는 함수를 그대로 가져다가 변경해볼게요
def outer(org_func):
    def inner(*args, **kwargs):
        print("추가하려는 기능 실행 시작")
        print(os.getcwd())
        print("추가하려는 기능 실행 종료")
        return org_func(*args, **kwargs)
    return inner


#original function
@outer
def func4(li):
    sum = 0
    for l in li:
        sum += l
    result = sum//len(li)
    print("리스트의 평균은 : {}".format(result))


#outer 함수의 호출이 없는 것에 주목하세요
func4([4, 4, 10, 10, 12, 16])
func4([5, 5, 5, 5, 5])
print(func4.__name__)





