#using decorator
'''
class Person:
    def __init__(self, name, money):
        self. name = name
        self. money = money
        
    @property
    def money(self):
        print("getter")
        return self._money
    
    @money.setter
    def money(self, money):
        print("setter")
        if money >=0:
            self._money = money
        else :
            self._money = 0
            
    def __repr__(self):
        return "name : {} \nmoney : {}".format(self.name, self.money)

if __name__ == "__main__":
    p1 = Person("yang", -5000)
    print(p1)
    
    p1.money = 1000
    print(p1)
'''

#property()
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def get_money(self):
        return self.__money

    def set_money(self, money):
        if money >= 0:
            self.__money = money
        else:
            self.__money = 0
    def __repr__(self):
        return "name : {} \nmoney : {}".format(self.name, self.money)

    money = property(get_money, set_money)

if __name__ == "__main__":
    p1 = Person("greg", -5000)
    p2 = Person("kim", 1000)
    print(p1)
    print(p2)

    p1.money = 2000

    print(p1)
    print(p2)
    

