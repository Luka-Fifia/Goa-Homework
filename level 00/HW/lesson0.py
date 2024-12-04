from turtle import *
speed(10)
#I paint a HOUSE

#Drawing Front Wall
width(5)
color("gray")
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#drawing a DOOR

penup()
goto(70, 5)
pendown()
color("orange")

right(180)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

penup()
goto(80, 35)
pendown()
left(90)
forward(10)

#drawing a ROOF

color("red")
penup()
goto(200,200)
pendown()
left(130)
forward(155)
left(100)
forward(155)


exitonclick()