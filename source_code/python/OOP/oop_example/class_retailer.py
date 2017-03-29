from class_person import Person

class Retailer(Person):
    price = 1000
    
    def __init__(self, name, age, money, product):
        super(Retailer, self).__init__(name, age, money)
        self.product = product

    def transaction(self, other, how_many):
        #클래스 변수 : 객체 or 클래스를 통해 접근 가능
        if self.product >=how_many and other.money >= self.price * how_many:
            self.product -= how_many
            other.product += how_many
            
            self.money += self.price * how_many
            other.money -= self.price * how_many

    def __str__(self):
        return '''
My name is {name}, {age} years old, and I am a retailer
I have {product} products and {money} won
'''.format(name = self.name, age = self.age, product = self.product, money = self.money)


   
    
