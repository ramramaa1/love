
import turtle

      


import math

def lovecurve(t):
    x = 16 * (math.sin(t)**3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x,y

turtle.setup(800,800)
turtle.title("Love Drawing")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor("red")
turtle.speed(1)


factor = 20
turtle.penup()
for i in range(0, 400):
    x,y = lovecurve(i)
    turtle.goto(x * factor , y * factor)

    turtle.pendown()
turtle.exitonclick()