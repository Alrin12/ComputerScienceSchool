#typical type
'''
def outer(func):
    def inner(*args, **kwargs):
        print("inner")
        return func(*args, **kwargs)
    return inner

@outer
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
'''

#decorator with arguments
'''
def dec(*ars):
    def outer(func):
        print("outer")
        def inner(*args, **kwargs):
            print("inner")
            print(ars)
            return func(*args, **kwargs)
        return inner
    return outer


@dec('a', 'b', 'c')
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
'''

#decorator in class
def dec(*ars):
    def outer(func):
        print("outer")
        def inner(self, *args, **kwargs):
            print("inner")
            print(ars)
            return func(self, *args, **kwargs)
        return inner
    return outer

class Base:
    @dec('a', 'b', 'c')
    def add(self, *args):
        sum = 0
        for arg in args:
            sum += arg
        return sum


b = Base()
result = b.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


