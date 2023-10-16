from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
scoreboard = ScoreBoard()


def main():
    screen.setup(600, 600)
    screen.bgcolor((0.2, 0.2, 0.2))
    screen.title("Snake Game")
    screen.tracer(0)

    snake.birth()
    food = Food()
    end_game = False

    while not end_game:
        snake.move()
        snake.event_listener(screen)
        if snake.head.distance(food) < 15:
            snake.add_segment()
            food.refresh()
            scoreboard.add()
        if snake.is_out(300, 300) or \
                snake.collision_with_tail():
            scoreboard.end_the_game()
            end_game = True
        screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
