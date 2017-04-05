my_name = "greg"
your_name = "matt"

my_age = 18
your_age = 25

my_money = 5000
your_money = 1000

#"나와 '연관'있는 데이터들만 모으고 너와 '연관' 있는 데이터들 모아 놓으면"
#나중에 변수를 다루기가 훨씬 수월하겠구나!!

my_dic = {"name" : "greg", "age" : 18, "money" : 5000}
your_dic = {"name" : "matt", "age" : 25, "money" : 1000}

#dic 사용하는 함수
#돈을 주는 "행동 or 기능"을 구현
def give_money(give_dic, receive_dic, money):
    give_dic.update({"money" : give_dic.get("money") - money})
    receive_dic.update({"money" : receive_dic.get("money") + money})
    
give_money(my_dic, your_dic, 2000)

print("my money : {}".format(my_dic["money"]))
print("your money : {}".format(your_dic["money"]))

#돈은 준다는 give_money라는 함수도
#나와 "연관"이 있구나!
#그렇다면 나와 연관이 있는 모든 변수와 함수를 모아보자!!

my_dic["function_1"] = give_money
your_dic["function_1"] = give_money

my_dic["function_1"](my_dic, your_dic, 1000)

print("my money : {}".format(my_dic["money"]))
print("your money : {}".format(your_dic["money"]))

def make_ones_dic(name, age, money, function):
    dic = dict(name = name, age = age, money = money, function_1 = function)
    return dic

his_dic = make_ones_dic("jason", 55, 400, give_money)
print(his_dic)
her_dic = make_ones_dic("sara", 22, 20000, give_money)
print(her_dic)



