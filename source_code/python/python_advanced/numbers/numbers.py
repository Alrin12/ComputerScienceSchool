num1 = 0xaa
num2 = 0b10101010
#print(bin(num1))
#print(bin(num2))

num3 = 170
#print(bin(170))

real = 10
comp = complex(real)
#print(comp)


#에러가 난다
#int('123.45')

int(float('123.45'))

a = 12.34
isinstance(a, float)


#float형 정보
import sys

#print(sys.float_info)
#print(sys.int_info)

#무한대의 표현 방법
#print(float("inf"))
#print(float("-inf"))

#float에서 정수인지 아니면 실수인지 확인
a = 12.567
#print(a.is_integer())
a = 12.0
#print(a.is_integer())

#반올림
a = 12.67
#print(round(a))

#내림
import math
#print(math.floor(a))


#올림
#print(math.ceil(a))
