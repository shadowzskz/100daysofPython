from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

start_pos = [(0,0), (-20, 0), (-40,0)]
segments = []
# Create snake
for pos in start_pos:
    new_seg = Turtle(shape="square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append((new_seg))

#NEW CODE

game_on = True
while(game_on):
    screen.update()
    time.sleep(0.1)
# Move snake
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(10)
screen.exitonclick()