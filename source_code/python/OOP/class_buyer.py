from class_person import Person

class Buyer(Person):
    def __init__(self, name, age, money, product):
        Person.__init__(self, name, age, money)
        self.product = product

    def Buy(self, other, how_many):
        if self.money >= other.price * how_many and other.product >=how_many:
            self.product += how_many
            other.product -= how_many
            
            self.money -= other.price * how_many
            other.money +=other.price * how_many
            

    def showMyInfo(self):
        print("My name is {0}, {1} years old, and I am a buyer".format(self.name, self.age))
        print("I have {0} products, and {1} won".format(self.product,  self.money))
