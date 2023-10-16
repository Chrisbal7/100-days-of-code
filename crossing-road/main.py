import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
player = Player()
scoreboard = ScoreBoard()


def main():
    screen.setup(width=600, height=600)
    screen.tracer(0)

    car_manager = CarManager()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        car_manager.generate_cars()
        for car in car_manager.cars:
            car_manager.move(car)
            if car.distance(player) <= 20:
                game_is_on = False
                scoreboard.game_over()
                break
        player.event_listener(screen)
        if player.has_finished():
            scoreboard.level_up()
            car_manager.increase_speed()
        screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
