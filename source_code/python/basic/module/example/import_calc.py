import calc

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

print("a + b = {}".format(calc.add(a, b)))
print("a - b = {}".format(calc.subtract(a, b)))
print("a * b = {}".format(calc.multiply(a, b)))
print("a // b = {}".format(calc.divide(a, b)))
