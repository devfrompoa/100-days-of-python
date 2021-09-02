import turtle
from turtle import Turtle, Screen
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

spot = Turtle()
spot.penup()
spot.hideturtle()
turtle.colormode(255)


def print_spots():
    new_color = random.choice(color_list)
    spot.color(new_color)
    spot.dot(20, new_color)
    spot.forward(50)


spot.speed("fastest")

x_position = -200.00
y_position = -250.00

# Print 10 x 10 rows of spots
# each dots around 20 in size and spaced about 50 paces
for _ in range (10):
    spot.setx(x_position)
    y_position += 50
    spot.sety(y_position)
    for _ in range(10):
        print_spots()



screen = Screen()
screen.exitonclick()




