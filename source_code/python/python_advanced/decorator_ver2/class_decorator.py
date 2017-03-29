class Deco:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print("__call__")
        return self.func(*args, **kwargs)

@Deco
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

        
