import turtle
from turtle import Turtle, Screen

raph = Turtle()
raph.shape("arrow") ## 'trutle', 'triangel', 'arrow', ....
raph.color("red")
# raph.forward(100)
# raph.right(90)
# raph.forward(100)
# raph.right(90)
# raph.forward(100)
# raph.right(90)
# raph.forward(100)

for _ in range(4):
    raph.forward(100)
    raph.right(90)

screen = Screen()
screen.exitonclick()