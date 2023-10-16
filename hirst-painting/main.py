# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def main():
    turtle.speed("fastest")
    draw_hirst_spots(12, 7, 400, 245)
    screen.mainloop()


def draw_hirst_spots(x_dots, y_dots, width=445, height=267):
    colors = generate_colors(100)
    # set initial position
    turtle.pu()
    turtle.setposition(-width / 2, - height / 2)
    turtle.pd()
    for i in range(y_dots):
        for _ in range(x_dots):
            draw_circle(8, random.choice(colors))
            turtle.pu()
            turtle.fd(width / x_dots)
            turtle.pd()
        turtle.penup()
        turtle.setheading(90)
        turtle.fd(height / y_dots)
        turtle.setheading(180)
        turtle.fd(width)
        turtle.setheading(0)
        turtle.pd()

    screen.mainloop()


def generate_colors(numbers):
    colors = []
    for _ in range(numbers):
        color = []
        for i in range(3):  # RGB
            color.append(random.randint(0, 255) / 255)
        colors.append(tuple(color))
    return colors


def draw_circle(diameter, color):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(diameter)
    turtle.end_fill()
    turtle.pu()


if __name__ == "__main__":
    main()
