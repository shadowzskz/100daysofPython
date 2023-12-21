import random
import turtle as t



t.colormode(255)
directions = [0, 90, 180, 270]
pensize = 1

def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return (red, green, blue)


for _ in range(200):
    t.pensize(pensize)
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))
    pensize = pensize + 1
    if (pensize == 10):
        pensize = 1