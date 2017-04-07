#공통 속성을 뽑아서 부모 클래스
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    
    def give_money(self, other, how_much):
        if self.money >= how_much:
            self.money -= how_much
            other.money += how_much
        else:
            print("나 돈 없어서 못 줘")
        
    def __str__(self):
        return '''
My name is {}
I am {} years old
I have {} won'''.format(self.name, self.age, self.money)
    
if __name__=="__main__":
    p1 = Person("greg", 18, 5000)
    p2 = Person("kim", 22, 1000)
    print(p1)
    print(p2)
    p1.give_money(p2, 2000)
    print(p1)
    print(p2)