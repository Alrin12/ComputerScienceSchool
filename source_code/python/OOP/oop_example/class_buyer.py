from class_person import Person

class Buyer(Person):
    def __init__(self, name, age, money, product):
        super(Buyer, self).__init__(name, age, money)
        self.product = product

    def transaction(self, other, how_many):
        total = other.price * how_many
        
        if self.money >= total and other.product >=how_many:
            self.product += how_many
            other.product -= how_many

            self.giveMoney(other, total)

    def __str__(self):
        return '''
My name is {name}, {age} years old, and I am a buyer
I have {product} products, and {money} won
'''.format(name = self.name, age = self.age, product = self.product, money = self.money)

