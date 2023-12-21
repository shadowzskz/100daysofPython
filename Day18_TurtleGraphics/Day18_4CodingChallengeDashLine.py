from turtle import Turtle, Screen

raph = Turtle()
raph.shape("arrow") ## 'trutle', 'triangel', 'arrow', ....
raph.color("red")
for _ in range(10):
    raph.forward(10)
    raph.penup()
    raph.forward(10)
    raph.pendown()
screen = Screen()
screen.exitonclick()