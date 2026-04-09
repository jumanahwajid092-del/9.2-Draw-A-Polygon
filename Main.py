from turtle import *


def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)
    turtle.end_fill()


screen = Screen()
screen.bgcolor("Maroon")
screen.setup(500, 500)


pen = Turtle()
pen.speed(0)
pen.color("Black")
pen.hideturtle()

name = Turtle()
name.speed(1)
name.color("white")
name.hideturtle()

while True:
    sides = int(input("How many sides does the polygon have? "))
    pen.clear()
    if sides == 3:
        regular_polygon(pen, sides)
        name.write("TRIANGLE", font = ("Times New Roman", 20))


screen.exitoniclick()
    


