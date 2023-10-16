from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self, car):
        if car.xcor() >= -320:
            car.backward(self.speed)
        else:
            car.ht()
            self.cars.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def generate_cars(self, x=300):
        num = random.randint(1, 6)
        if num == 1:
            y = random.randint(-240, 240)
            self.cars.append(get_car(x, y))


def get_car(x, y):
    car = Turtle()
    car.shape("square")
    car.up()
    car.speed("fastest")
    car.shapesize(1, 2)
    car.color(random.choice(COLORS))
    car.goto((x, y))
    return car
