class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        
    def giveMoney(self, other,how_much):
        if how_much <=self.money:
            other.money +=how_much
            self.money -= how_much
        else:
            print("you don't have {0}".format(how_much))

    def showMyInfo(self):
        print("{0} has {1}".format(self.name, self.money))


if __name__ == "__main__":
    p1 = Person("taehwan", 35, 5000)
    p2 = Person("greg", 21, 2000)

    p1.giveMoney(p2, 3000)

    p1.showMyInfo()
    p2.showMyInfo()


            
