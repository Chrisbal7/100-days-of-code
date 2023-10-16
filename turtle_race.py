from turtle import Turtle, Screen
import random

colours = ["purple", "blue", "green",
           "yellow", "orange", "red"]
screen = Screen()


def main():
    screen.setup(600, 400)
    my_bet = ""
    while my_bet not in colours:
        my_bet = screen.textinput(title="Make your bet",
                                  prompt="Which turtle will win the race?")
        if my_bet:
            my_bet = my_bet.lower().strip()

    turtles = []
    for colour in colours:
        new_turtle = Turtle(shape="turtle")
        new_turtle.pu()
        new_turtle.color(colour)
        new_turtle.shapesize(1.5)
        new_turtle.steps = 0
        turtles.append(new_turtle)

    for i in range(len(turtles)):
        t = turtles[i]
        t.setposition((-280, -150))
        y_position = t.ycor() + (i + 1) * 50
        t.sety(y_position)

    end_race = False
    while not end_race:
        for turtle in turtles:
            pace = random.randint(0, 20)
            turtle.fd(pace)
            turtle.steps += pace
            if turtle.steps >= screen.window_width() - 20:
                end_race = True
                print(f"The {turtle.color()[1]}'s turtle win the race")
                if turtle.color()[1] == my_bet:
                    print("You're right, you win the bet")
                else:
                    print("You lose, oops!")
                break
    screen.exitonclick()


if __name__ == "__main__":
    main()
