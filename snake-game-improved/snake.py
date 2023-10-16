import time
from turtle import Turtle


class Snake:
    def __init__(self):
        # Create an initial snake
        self.segments = []
        self.length = len(self.segments)
        self.head = None
        self.tail = None

    def move(self):
        if not self.is_out(300, 300):
            for i in range(len(self.segments) - 1, 0, -1):
                time.sleep(0.05)
                segment = self.segments[i]
                previous_seg = self.segments[i - 1]
                new_coordinates = previous_seg.position()
                segment.setposition(new_coordinates)
            self.head.fd(20)

    def add_segment(self, num=1):
        for _ in range(num):
            length = len(self.segments)
            segment = Turtle(shape="square")
            segment.pu()
            segment.shapesize(1)
            segment.color("wheat")
            segment.setposition(- length * 20, 0)
            self.segments.append(segment)

    def is_out(self, x, y):
        if abs(self.head.xcor()) > x or \
                abs(self.head.ycor()) > y:
            return True
        return False

    def collision_with_tail(self):
        for tail in self.tail:
            if self.head.distance(tail) <= 10:
                return True
        return False

    def birth(self):
        self.add_segment(3)
        self.head = self.segments[0]
        self.tail = self.segments[1:]

    def event_listener(self, screen):
        screen.listen()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")
        screen.onkey(fun=self.right, key="Right")
        screen.onkey(fun=self.left, key="Left")

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
