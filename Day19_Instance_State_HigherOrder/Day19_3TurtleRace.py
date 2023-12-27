import random
import turtle
from turtle import Turtle,Screen
import random

israce = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle to win the race? Enter the color: red, orange. yellow, green, purple, blue")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_create in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_create])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_pos[turtle_create])
    turtle_list.append(new_turtle)


if user_bet:
    israce = True

while israce:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            israce = False
            win_turtle = turtles.pencolor()
            if win_turtle == user_bet:
                print(f"You won the bet {user_bet} turtle won")
            else:
                print(f"You lost the bet {win_turtle} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)

screen.listen()
screen.exitonclick()
