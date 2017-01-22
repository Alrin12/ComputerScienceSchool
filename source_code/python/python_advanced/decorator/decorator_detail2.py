#데코레이터에 대해서 이해를 했다면 한 가지 궁금한 점이 생깁니다
#여러가지 functionality를 추가할 수는 없을까?
#마치....처럼요
'''
@func1
@func2
@func3
@func4
def org_func(...):
    print("aaaa")

'''

#실제로 파이썬에서는 이와 같은 문법이 가능합니다.
#하지만 사용할 때 한 가지 주의사항이 있는데 이번 시간에는
#왜 이와 같이 써야 하는지에 대해 차근차근 배워보도록 하겠습니다.

def increase_two(org_func):
    def inc_inner(**kwargs):
        a, b = kwargs.keys()
        kwargs[a] += 2
        kwargs[b] += 2
        return org_func(**kwargs)
    return inc_inner

def square_two(org_func):
    def sq_inner(**kwargs):
        a, b = kwargs.keys()
        kwargs[a] **= 2
        kwargs[b] **= 2
        return org_func(**kwargs)
    return sq_inner

'''
#case 1
@increase_two
def showInfo(a, b):
    print(" a = {0}, b = {1}".format(a, b))

#결과 값은 5, 7
showInfo(a = 3, b = 5)

'''

'''
#case 2
@square_two
def showInfo(a, b):
    print(" a = {0}, b = {1}".format(a, b))


showInfo(a = 3, b = 5)
'''


'''
#case 3
#내가 하고 싶은 것은
#먼저 2를 더한 후 제곱, 즉 (3 + 2)의 제곱과 (5 + 2)의 제곱이므로
#출력 예상 값은 a = 25, b = 49
@increase_two
@square_two
def showInfo(a, b):
    print(" a = {0}, b = {1}".format(a, b))


showInfo(a = 3, b = 5)
'''


#case 4
#내가 하고 싶은 것은
#먼저 제곱한 후 2를 더한 것, 즉 9 + 2와 25 + 2 이므로
#출력 예상 값은 a = 11, b = 27
@square_two
@increase_two
def showInfo(a, b):
    print(" a = {0}, b = {1}".format(a, b))


showInfo(a = 3, b = 5)



