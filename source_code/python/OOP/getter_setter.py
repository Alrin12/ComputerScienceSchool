class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        #getter 함수 호출
        self.money = money

    #getter
    @property
    def money(self):
        print("getter of money")
        return self._money
    
    #setter
    @money.setter
    def money(self, mon):
        print("setter of money")
        if mon <0:
            self._money = 0
        elif mon > 10000:
            self._money = 10000
        else:
            self._money = mon
        
    def giveMoney(self, other,how_much):
        if how_much <=self.money:
            other._money +=how_much
            self._money -= how_much
        else:
            print("you don't have {0}".format(how_much))

    def showMyInfo(self):
        print("{0} has {1}".format(self.name, self._money))

if __name__ == "__main__":
    #setter 호출
    #getter 호출
    p1 = Person('greg', 35, -300)
    print(p1.money)
    print('\n')
    
    #setter 호출
    p1.money = 100000
    print('\n')
    
    #getter 호출
    money = p1.money
    print(money)
    print('\n')
    
    #정보은닉은 안됩니다.
    p1._money = 550
    print(p1._money)
    
