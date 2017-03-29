#일급함수
#1. able to be an argument
#2. able to be an return value
#3. abel to be stored in variables or data structures

def func(*args):
    for arg in args:
        print(arg, end = ' ')
    return args

variable = func #3. stored in an variable
variable(1, 2)

print()

def func2(f, *args):#1. passed as arguments
    f(*args)

func2(func, 1, 2, 3, 4, 5)

