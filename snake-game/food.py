from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue", "blue")
        self.shapesize(0.6)
        self.refresh()

    def refresh(self, x=280, y=280):
        self.goto(generate_random_coord(x, y))


def generate_random_coord(x, y):
    x = random.randint(-x, x)
    y = random.randint(-y, y)
    return (x, y)
