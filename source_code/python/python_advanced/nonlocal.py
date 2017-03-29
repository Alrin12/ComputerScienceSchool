
def outer():
    a = 10
    def inner():
        nonlocal a
        a = 20
        print(a)
    inner()

outer()
