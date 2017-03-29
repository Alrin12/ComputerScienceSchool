class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def get_money(self):
        print("getter executed!")
        return self._money

    def set_money(self, money):
        print("setter executed!")
        if money < 0:
            self._money = 0
        else:
            self._money = money

    def __str__(self):
        return "{} has {} won".format(self.name, self._money)

    money = property(get_money, set_money)


p1 = Person("greg", -4000)
print(p1)
p1.money = 5000
print(p1)

