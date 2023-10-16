from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from variables import x

screen = Screen()
ball = Ball()
paddler1 = Paddle("left")
paddler2 = Paddle("right")
scoreboard = ScoreBoard()


def main():
    screen.setup(800, 600)
    screen.bgcolor("black")
    paddler1.goto(-x, 0)
    paddler2.goto(x, 0)

    end_game = False

    while not end_game:
        ball.move()
        if 90 < ball.heading() < 270:
            paddles = [paddler1, paddler2]
        else:
            paddles = [paddler2, paddler1]

        if not ball.collision_with_paddle(paddles[0]):
            if abs(ball.xcor()) >= x + 20:
                paddles[1].add_score()
                ball.reflect()
                continue
            paddles[0].event_listener(screen)

    screen.exitonclick()


if __name__ == "__main__":
    main()
