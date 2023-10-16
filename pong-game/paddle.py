from turtle import Turtle
from variables import y


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 2)
        self.pu()
        self.speed("fastest")
        self.setheading(90)

        self.score_marker = Turtle()
        self.score_marker.color("white")
        self.score_marker.ht()
        self.score = 0
        self.player_side = side
        self.display_score()

    def event_listener(self, screen):
        screen.listen()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")

    def up(self):
        self.setheading(90)
        if self.ycor() < y:
            self.fd(20)

    def down(self):
        self.setheading(270)
        if self.ycor() > - y:
            self.fd(20)

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.score_marker.clear()
        self.score_marker.pu()
        if self.player_side == "left":
            self.score_marker.goto(-40, 240)
        elif self.player_side == "right":
            self.score_marker.goto(40, 240)
        self.score_marker.pd()
        self.score_marker.write(arg=f"{self.score}",
                                font=("Press Start 2P", 40, "normal"),
                                align="center")
