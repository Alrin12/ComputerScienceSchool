class Person:
    #클래스 변수 : 모든 객체가 공유한다
    planet = 'Earth'
    
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    # class method : 첫번째 매개변수로 class를 자동으로 받는다.
    # 주로 생성자 오버로딩으로 쓰인다.(파이썬에서는 원칙적으로 생성자 오버로딩 안됨)
    @classmethod
    def FromString(cls, string):
        name, age_int, money_int = string.split('-')
        age = int(age_int)
        money = int(money_int)
        return cls(name, age, money)

    #클래스 변수의 값을 변경할 때 사용한다.
    @classmethod
    def ChangePlanet(cls, pln):
        cls.planet = pln

    #static method : 전역변수처럼 쓸 수 있다.
    # 클래스와 관련있을 경우 클래스 내에 선언(캡슐화)
    @staticmethod
    def SavingCalculator(amount_per_month, months):
        return amount_per_month * months

    #객체함수에서도 static 함수를 불러와 쓸 수 있다.
    def PredictMoney(self, apm, mons):
        return self.money + Person.SavingCalculator(apm, mons)
    
    def giveMoney(self, other,how_much):
        if how_much <=self.money:
            other.money +=how_much
            self.money -= how_much
        else:
            print("you don't have {0}".format(how_much))

    def showMyInfo(self):
        print("{0} has {1}".format(self.name, self.money))


if __name__ == "__main__":
    #p1 = Person('greg', 35, 5000)
    p1 = Person.FromString("greg-35-5000")
    p1.showMyInfo()

    #class 함수 호출
    #클래스로 호출한다
    #객체로도 호출 가능하지만 이렇게는 절대 호출하지 않는다.
    #p1.ChangePlanet('Mars')
    Person.ChangePlanet('Mars')
    print(Person.planet)

    #static 함수 호출
    saving_money = Person.SavingCalculator(100, 12)
    print(saving_money)

    print(p1.PredictMoney(100, 10))
    

            
