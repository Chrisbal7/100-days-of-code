from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.speed("fastest")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def event_listener(self, screen):
        screen.listen()
        screen.onkey(key="Up", fun=self.move)

    def reset(self):
        self.goto(STARTING_POSITION)

    def has_finished(self):
        if self.ycor() >= 280:
            self.reset()
            return True
        return False
