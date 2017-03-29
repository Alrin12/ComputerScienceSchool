class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("destructor")
    #객체를 대표해서 유일한 문자열
    #__str__ 없으면 대신 호출
    def __repr__(self):
        print("__repr__")
        return "my name is {} \n i am {} years old".format(self.name, self.age)
    #사용자 편의
    #print() 호출 시 호출
    #__repr__를 대신할 수 없다
    def __str__(self):
        print("__str__")
        return "My name is {} \nI am {} years old".format(self.name, self.age)

if __name__ == "__main__":
    p1 = Person("greg", 33)

    #__str__
    print(p1)
    str(p1)

    #__repr__
    repr(p1)
