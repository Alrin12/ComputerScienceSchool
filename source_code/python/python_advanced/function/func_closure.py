#closure
# providing function objects
#with nonlocal-variables or caches in symbol-tables

import math

def sqrt_s():
    cache = {}
    def func(x):
        if x in cache:
            print("saved one : ", end = '')
            return cache[x]
        else:
            cache[x] = math.sqrt(x)
            return cache[x]
    return func

sqrt_func = sqrt_s()

print("{0:.3f}".format(sqrt_func(5)))
print("{0:.3f}".format(sqrt_func(5)))
print("{:.3f}".format(sqrt_func(15)))
print("{:.3f}".format(sqrt_func(15)))
