from turtle import Turtle, Screen

ralph = Turtle()
screen = Screen()

def move_forward():
    ralph.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
