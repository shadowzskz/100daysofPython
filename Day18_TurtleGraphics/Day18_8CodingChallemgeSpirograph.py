import random
import turtle as t
from turtle import Screen



t.colormode(255)
directions = [0, 90, 180, 270]
pensize = 1
t.speed("fastest")

def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, green, blue)


def drawCircle(size):
    for _ in range(int(360 / size)):
        t.color(random_color())
        t.circle(80)
        t.setheading(t.heading() + size)


drawCircle(10)
screen = Screen()
screen.exitonclick()
