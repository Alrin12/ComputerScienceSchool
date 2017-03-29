li = [1, 2, 3, 4, 5]
print("{}, {}".format(min(li), max(li)))

print("sqrt({}) : {}".format(2, 2** 0.5))

#자릿수 
print("sqrt({0:3}) : {1:0.5}".format(2, 2** 0.5))

#자료형 
print("sqrt({0:d}) : {1:f}".format(2, 2** 0.5))

#자료형 + 자릿
print("sqrt({0:3d}) : {1:0.2f}".format(2, 2** 0.5))

#1,234,567,890
a = 1234567890
print("{0:,d}".format(a))

#list가 인자로 전달될 때
print("{0[4]} is the next value of {0[3]}".format(li))

#kw 인수일 경우 (순서 상관 없다)
print("{name} is {age} years old".format(age = 33, name = "greg"))

#모듈의 경우
import sys
print("{0.float_info.max}".format(sys))

print("{0.__doc__}".format(list))
