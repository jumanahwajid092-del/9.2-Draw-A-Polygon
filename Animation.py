from turtle import *
import random

def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    yertle = Turtle()
    yertle.color("Black")
    yertle.pensize(30)
    yertle.speed(0)
    yertle.hideturtle()
    yertle.penup()
    yertle.goto(-250, 250)
    yertle.pendown()
    yertle.goto(240, 250)
    yertle.goto(245, -245)
    yertle.goto(-250, -245)
    yertle.goto(-250, 245)
    
    

def move_forward(turtle):
    turtle.forward(5)

    if turtle.xcor() > - 235 or turtle.xcor() < -235:
        turtle.speed(0)
        turtle.setheading(180 - turtle.subheading())

    if turtle.ycor() > - 235 or turtle.ycor() < -235:
        turtle.speed(0)
        turtle.setheading(-turtle.subheading() )

        turtle.forward(10)
        turtle.speed(1)

def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 240 or newX < -240:
        deltaX *= -1
        newX = turtle.xcor()
    if newY > 240 or newY < -240:
        deltaY *= -1
        newY = turtle.ycor()
    turtle.goto(newX, newY)
    return deltaX, deltaY

screen = Screen()
screen.bgcolor("Maroon")
screen.setup(500, 500)

playing_area()

pickel = Turtle()
pickel.color(generate_random_hex_color())
pickel.shape("triangle")
pickel.setheading( random.randint(0,360))
deltaX = random.randint(-5, 5)
deltaY = random.randint(-5, 5)



while True:
    deltaX, deltaY = move_xy(pickel, deltaX, deltaY)

screen.exitonclick()
