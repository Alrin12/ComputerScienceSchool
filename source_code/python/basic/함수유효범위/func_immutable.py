a = 10
b = 5
c = 7

def func(a, b):
    print('a = {0}, b = {1} before change in func'.format(a, b)) 
    a, b = b, a
    print('a = {0}, b = {1} after change in func'.format(a, b))
    c = 27
    print('c = {} after change in func'.format(c))

print('a = {0}, b = {1} before'.format(a, b))
print('c = {} before'.format(c))
print("\n")

func(a, b)
print("\n")
print('a = {0}, b = {1} after'.format(a, b))
print('c = {} after'.format(c))
