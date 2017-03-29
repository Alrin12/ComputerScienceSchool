import sys

x = 0

try:
    1/x
except:
    print(sys.exc_info()[1])
finally:
    #무조건 실행된다
    print("execute unconditionally")


