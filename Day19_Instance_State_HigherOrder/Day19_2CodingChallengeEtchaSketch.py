#Coding Challenge
#input: WSAD to move
#Output: Move forwared, backward, cc,c

from turtle import Turtle,Screen

ralph = Turtle()
screen = Screen()

def move_forward():
    ralph.forward(10)

def move_backward():
    ralph.backward(10)

def move_CC():
    # ralph.right(10)
    # ralph.forward(10)
#     ALTERNATIVE
    new_heading = ralph.heading() + 10
    ralph.setheading(new_heading)

def move_C():
    new_heading = ralph.heading() - 10
    ralph.setheading(new_heading)


def clear():
    ralph.clear()
    ralph.penup()
    ralph.home()
    ralph.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_CC)
screen.onkey(key="d", fun=move_C)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
