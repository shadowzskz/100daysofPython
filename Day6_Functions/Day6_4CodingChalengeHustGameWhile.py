def turn_right():
    turn_left()
    turn_left()
    turn_left()


def task():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    task()
