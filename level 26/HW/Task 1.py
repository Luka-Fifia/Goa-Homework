from turtle import *
speed(10)
penup()
goto(-950,0)
pendown()

def triangle():
    forward(50)
    left(139)
    forward(40)
    left(92)
    forward(35)
    left(129)
    penup()
    forward(60)
    pendown()


for i in range(1,120):
    if i % 2 == 0:
        color("green")
    else:
        color("blue")
    triangle()


exitonclick()