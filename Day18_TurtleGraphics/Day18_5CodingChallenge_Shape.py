import turtle
from turtle import Turtle, Screen
import random

raph = Turtle()
raph.shape("arrow") ## 'trutle', 'triangel', 'arrow', ....
colors = ["red", "green", "black", "wheat"]

total_angle = 360
sides = 3

def draw(sides):
    shape: int = int(total_angle / sides)
    for _ in range(sides):
        raph.forward(100)
        raph.right(shape)

while sides <=10:
    raph.color(random.choice(colors))
    draw(sides)
    sides += 1



screen = Screen()
screen.exitonclick()