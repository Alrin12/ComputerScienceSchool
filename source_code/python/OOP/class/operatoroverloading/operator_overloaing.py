class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, n):
        return Point(self.x + n, self.y + n)
    
    def __radd__(self, n):
        return Point(self.x + n, self.y + n)
    
    def __sub__(self, n):
        return Point(self.x - n, self.y - n)
    
    def __rsub__(self, n):
        return Point(n - self.x, n - self.y)
    
    def __mul__(self, n):
        return Point(self.x * n, self.y * n)
    
    def __rmul__(self, n):
        return Point(self.x * n, self.y * n)
    
    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)
    
    def __rtruediv__(self, n):
        return Point(n / self.x, n / self.y)
    
    def __floordiv__(self, n):
        return Point(self.x // n, self.y // n)
    
    def __rfloordiv__(self, n):
        return Point(n // self.x, n // self.y)
        
    def __mod__(self, n):
        return Point(self.x % n, self.y % n)
    
    def __rmod__(self, n):
        return Point(n % self.x, n % self.y)
    
    def __str__(self):
        return "( {}, {} )".format(self.x, self.y)
    
if __name__ == "__main__":
    p = Point(10, 10)
    print(p)
    
    p2 = p + 2
    print(p2)

    p3 = 2 + p
    print(p3)

    p4 = p - 6
    print(p4)


    p5 = 16 - p
    print(p5)

    p6 = p * 5
    print(p6)

    p7 = 5 * p
    print(p7)

    p8 = p/2
    print(p8)

    p9 = 100/p
    print(p9)

    p10 = p//2
    print(p10)

    p11 = 50//p
    print(p11)

    p12 = p % 3
    print(p12)

    p13 = 13 % p
    print(p13)
