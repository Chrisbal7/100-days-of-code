from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("arrow")
        self.shapesize(0.2)
        self.ht()
        self.up()
        self.pencolor("SlateGray")
        self.setposition(0, 260)
        self.refresh()

    def add(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                       move=False, align='center',
                       font=('Arial', 18, 'normal'))

    def end_the_game(self):
        self.pencolor("IndianRed")
        self.goto(0, 0)
        self.write(arg="GAME  OVER",
                       move=False, align='center',
                       font=('Arial', 28, 'normal'))
