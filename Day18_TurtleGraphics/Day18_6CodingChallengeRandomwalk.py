import turtle
from turtle import Turtle, Screen
import random

raph = Turtle()
raph.shape("arrow") ## 'trutle', 'triangel', 'arrow', ....
colors = ["red", "green", "black", "wheat", "lightgreen", "turquoise", "skyblue", "tomato", "purple"]
directions = [0, 90, 180, 270]
pensize = 1
raph.speed("fastest")

for _ in range(200):
    raph.pensize(pensize)
    raph.color(random.choice(colors))
    raph.forward(30)
    raph.setheading(random.choice(directions))
    pensize = pensize + 1
    if (pensize == 10):
        pensize = 1

screen = Screen()
screen.exitonclick()
