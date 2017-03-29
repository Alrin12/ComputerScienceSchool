class Animal:
    def Say(self):
        print("I say .....")

class Dog(Animal):
    def Say(self):
        print("I say BOW-WOW")

class Cat(Animal):
    def Say(self):
        print("I say MEW MEW")

class Duck(Animal):
    def Say(self):
        print("I say QUACK QUACK")

class Lion(Animal):
    pass

if __name__ == "__main__":
    animals = []

    dog = Dog()
    cat = Cat()
    duck = Duck()
    lion = Lion()

    animals.append(dog)
    animals.append(cat)
    animals.append(duck)
    animals.append(lion)

    for animal in animals:
        animal.Say()

