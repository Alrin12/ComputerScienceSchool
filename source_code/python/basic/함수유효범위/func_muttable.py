

# 기존 list를 변경만 한다
def func(li):
    print("first li in func1 li = ", id(li))
    li[2] = 15
    li.remove(2)
    del li[0]
    li.append([11, 12, 13])
    print("second li in func1 li = ", id(li))



# 함수 안에서 새로운 list를 참조
def func2(li):
    print("first li in func2 li = ", id(li))
    li = [11, 12, 13]
    print("second li in func2 li = ", id(li))


a = [1, 2, 3, 4]

print("before func  --> a = ", id(a))
print("\n")

func(a)
#func2(a)

print("\n")
print("after func --> a = ", id(a))

print(a)






print("\n\ndictionary is same!!")

b = { 1 : 'greg'}

def func3(dic):
    name = input("put a name on the console : ")
    dic[2] = name

print(b)
func3(b)
print("\n")
print(b)
