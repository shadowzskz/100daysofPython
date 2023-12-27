from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_pos = [(0,0), (-20, 0), (-40,0)]

for pos in start_pos:
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.goto(pos)


screen.exitonclick()