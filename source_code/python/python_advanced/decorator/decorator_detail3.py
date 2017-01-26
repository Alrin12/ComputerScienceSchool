#마지막으로 데코레이터를 쓸 때 주의사항에 대해 알아보도록 하겠습니다

'''
def func1(org_func):
    def inner_1(*args, **kwargs):
        print("inner_1 start")
        print("org_func in inner_1 is {}".format(org_func.__name__))
        return org_func(*args, **kwargs)
    return inner_1

def func2(org_func):
    def inner_2(*args, **kwargs):
        print("inner_2 start")
        print("org_func in inner_2 is {}".format(org_func.__name__))
        return org_func(*args, **kwargs)
    return inner_2

@func1
@func2
def original_function():
    print("original function start")

original_function()
'''



#만약 제가 하고자 하는 결과가 각 함수에 전달되는 
# org_func이 계속해서 original_function이길 바란다면
#아래와 같이 코드를 추가하면 됩니다!


#original function을 계속 유지하는 방법
#wraps 데코레이터

'''
from functools import wraps


def func1(org_func):
    @wraps(org_func)
    def inner_1(*args, **kwargs):
        print("inner_1 start")
        print("org_func in inner_1 is {}".format(org_func.__name__))
        return org_func(*args, **kwargs)
    return inner_1

def func2(org_func):
    @wraps(org_func)
    def inner_2(*args, **kwargs):
        print("inner_2 start")
        print("org_func in inner_2 is {}".format(org_func.__name__))
        return org_func(*args, **kwargs)
    return inner_2

@func1
@func2
def original_function():
    print("original function start")

original_function()
'''
