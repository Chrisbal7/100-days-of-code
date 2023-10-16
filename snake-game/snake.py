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
        screen.onkey(fun=lambda: self.change_heading(90, 270), key="Up")
        screen.onkey(fun=lambda: self.change_heading(270, 90), key="Down")
        screen.onkey(fun=lambda: self.change_heading(0, 180), key="Right")
        screen.onkey(fun=lambda: self.change_heading(180, 0), key="Left")

    def change_heading(self, to_heading, except_heading):
        if self.head.heading() != except_heading:
            self.head.setheading(to_heading)

