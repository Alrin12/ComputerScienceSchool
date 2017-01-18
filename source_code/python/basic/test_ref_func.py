def func(a, b):
    print("a : {} b : {} before change in function".format(id(a), id(b)))
    a = 15
    print("a : {} b : {} after change in function".format(id(a), id(b)))


a = 10
b = 5
print("a : {} b : {} before function".format(id(a), id(b)))
func(a, b)

print("a : {} b : {} after function".format(id(a), id(b)))
