# *args의 형태
# tuple의 형태로 받는다
#인덱싱이나 for문으로 접근해 변수를 받아온다.
def func1(*args):
    print(args)
    for ele in args:
        print(ele)

# **kwargs의 형태
# dictionary의 형태로 받는다
def func2(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('[key : value]  >>>  {} : {}'.format(key, value))

# *args, **kwargs를 함께 쓰는 형태
def func3(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ =='__main__':
    #func1(1, 'a', 1.4, 'I am your father')
    #func2(name = 'greg', age = 34, money = 1000.45)
    func3(1, 1.14, name = 'greg', age = 34)
    func3(1, 'a', 1.4, 'I am your father')
    func3(name = 'greg', age = 34, money = 1000.45)
