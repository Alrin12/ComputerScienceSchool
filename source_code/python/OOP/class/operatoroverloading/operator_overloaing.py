class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "( {}, {} )".format(self.x, self.y)
    def __add__(self, n):
        print("__add__")
        self.x += n
        self.y += n
        return self
    
    def __radd__(self, n):
        print("__radd__")
        self.x += n
        self.y += n
        return self
    
p1 = Point(3, 3)
p2 = Point(0, 0)

print(p1)

p2 = p1 + 3
print(p2)

p2 = 3 + p1
print(p2)

