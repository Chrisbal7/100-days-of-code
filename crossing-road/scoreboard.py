from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-200, 240)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",
                   align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("Red")
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
