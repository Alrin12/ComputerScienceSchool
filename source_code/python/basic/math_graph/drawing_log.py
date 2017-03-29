from turtle import *
from math import *

SCALE = 30
list_x = [x * 0.01 for x in range(1, 1001)]

def magnify(x, y):
    _x = x*SCALE
    _y = y*SCALE
    return _x, _y

tracer(False)

while 1:

    reset()
    e_string = None
    #base를 입력받는다.
    base_string = input("base를 입력하세요(0 : 종료) : ")

    #자연상수
    if base_string == 'e':
        e_string = 'e'
        base_string = '2.718'
        
    base = eval(base_string)
    
    if base == 0:
        break

    while base == 1:
        base_string = input("base를 입력하세요(0 : 종료) : ")
        base = eval(base_string)

    #x축 선을 긋는다 : -10 ~ 10
    up()
    goto(-10 * SCALE, 0)
    down()
    forward(10 * 2 * SCALE)
    write('x')

    #y축 선을 긋는다 : -10 ~ 10
    up()
    goto(0, -10 * SCALE)
    left(90)
    down()
    forward(10 * 2 * SCALE)
    write('y')

    for x in list_x:
        y = log(x, base)
        up()
        _x, _y = magnify(x, y)
        goto(_x, _y)
        dot(2, 'red')

    if e_string == 'e':
        func_str = "ln" + ' X'
    else:
        func_str = "log" + base_string + 'X'

    write(func_str)

