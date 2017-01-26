'''
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def showInfo(self):
        print("{} has {} won".format(self.name, self.money))

#위와 같이 클래스를 설계한 상태에서
#인스턴스 하나를 만들 때

p = Person('greg', -3000)
p.showInfo()

#제가 하고 싶은 일은 money를 항상 양수로 유지하는 것
#생성 됐을 때도 음수는 아니게 만들고 싶습니다!
'''



class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    #getter 함수
    @property
    def money(self):
        print("getter executed")
        return self._money
    
    #setter 함수 
    @money.setter
    def money(self, mon):
        print("setter executed!")
        if mon < 0:
            self._money = 0
        else:
            self._money = mon

    def showInfo(self):
        print("{} has {} won".format(self.name, self._money))

if __name__ == "__main__":
    #setter 함수 호출
    p = Person('greg', -300)
    p.showInfo()

    print('\n\n')
    
    #getter 함수 호출
    #객체변수 처럼 쓰고 있지만 사실은 함수를 호출!!
    p.money

    print("\n\n")

    #물론 정보은닉이 되는 건 아닙니다
    p._money = 50
    p.showInfo()
     
