import random
import time

from turtle import Turtle
from variables import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.goto(0, random.randint(- y, y))
        self.setheading(random.randint(min_angle,
                                       max_angle))

    def move(self):
        self.forward(pace)
        time.sleep(0.05)
        if abs(self.ycor()) >= y:
            self.reflect()

    def reflect(self):
        heading = self.heading()
        if abs(self.ycor()) >= y and abs(self.xcor()) >= x + 20:
            self.setheading(- heading + 180)
        elif abs(self.ycor()) >= y:
            self.setheading(- heading)
        else:
            self.setheading(- heading + 180)

    def collision_with_paddle(self, paddle):
        if self.distance(paddle) < 40:
            self.reflect()
            return True
        print(self.position())
        return False
