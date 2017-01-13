from class_person import Person

class Retailer(Person):
    price = 1000
    
    def __init__(self, name, age, money, product):
        Person.__init__(self, name, age, money)
        self.product = product

    def Sell(self, other, how_many):
        if self.product >=how_many and other.money >= self.price * how_many:
            self.product -= how_many
            other.product += how_many
            
            self.money += self.price * how_many
            other.money -= self.price * how_many
            

    def showMyInfo(self):
        print("My name is {name}, {age} years old, and I am a retailer".format(name = self.name,
                                                              age = self.age))
        print("I have {0} products and {1} won".format(self.product, self.money))

   
    
