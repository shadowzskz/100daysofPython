#KEYWORD  MODULE    KEYWORD   THINGS_IN_MODULE
#from     turtle    import    Turtle
#IMPORT ALL
#from     turtle    import    *
#Change name
#from     turtle    as    T

from turtle import Turtle, Screen

turtle = Turtle()
turtle2 = Turtle()
turtle.shape("arrow")
turtle.forward(100)
turtle2.shape("turtle")
screen = Screen()
screen.exitonclick()