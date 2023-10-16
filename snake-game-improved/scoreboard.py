from turtle import Turtle
import os

PATH = "score.txt"
highest_score = 0
if os.path.exists(PATH):
    with open(PATH) as file:
        content = file.read()
    if content:
        highest_score = int(content)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = highest_score
        self.shape("arrow")
        self.shapesize(0.2)
        self.ht()
        self.up()
        self.pencolor("SlateGray")
        self.refresh()

    def add(self):
        self.score += 1
        self.update_highest_score()
        self.refresh()

    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(PATH, "w") as f:
                f.write(str(self.highest_score))

    def refresh(self):
        self.clear()
        self.setposition(-100, 260)
        self.write(arg=f"Score: {self.score}",
                   move=False, align='center',
                   font=('Arial', 18, 'normal'))
        self.goto(100, 260)
        self.write(arg=f"Highest score: {self.highest_score}",
                   move=False, align='center',
                   font=('Arial', 18, 'normal'))

    def end_the_game(self):
        self.pencolor("IndianRed")
        self.goto(0, 0)
        self.write(arg="GAME  OVER",
                   move=False, align='center',
                   font=('Arial', 28, 'normal'))
