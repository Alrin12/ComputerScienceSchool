from turtle import *
from math import *

SCALE = 30
list_x = [x * 0.01 for x in range(1, 1001)]

def magnify(x, y):
    _x = x*SCALE
    _y = y*SCALE
    return _x, _y

tracer(False)

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

# O(n^2)
for x in list_x:
    y = x**2
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, 'red')

goto(70, 200)
write("O(n^2)", font=("Arial", 12, "normal"))


# O(n*logn)
for x in list_x:
    y = x*log(x, 10)
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(3, 'blue')

goto(200, 140)
write("O(n*logn)", font=("Arial", 12, "bold"))



#O(n)
for x in list_x:
    y = x
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, 'green')

goto(170, 200)
write("O(n)", font=("Arial", 12, "normal"))


#O(logn)
for x in list_x:
    y = log(x, 10)
    up()
    _x, _y = magnify(x, y)
    goto(_x, _y)
    dot(2, 'purple')

goto(300, 20)
write("O(logn)", font=("Arial", 12, "normal"))


