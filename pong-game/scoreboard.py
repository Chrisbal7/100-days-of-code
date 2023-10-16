from turtle import Turtle
from variables import y


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.ht()
        self.penup()
        self.speed("fastest")
        self.pen(pencolor="white", pensize=3)
        self.goto(0, -y)
        self.setheading(90)
        self.draw_line()

    def draw_line(self):
        for i in range(15):
            self.fd(20)
            self.pd()
            self.fd(20)
            self.pu()



