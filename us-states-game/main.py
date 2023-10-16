import csv
from turtle import Screen, Turtle

screen = Screen()


class State:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (int(x), int(y))


def extract_data():
    states = []
    with open("50_states.csv") as csv_obj:
        reader = csv.reader(csv_obj)
        for name, x, y in reader:
            if reader.line_num == 1:
                continue
            state = State(name, x, y)
            states.append(state)
    return states


def get_writer():
    writer = Turtle()
    writer.ht()
    writer.up()
    return writer


def write(writer, state):
    writer.goto(state.position)
    writer.write(arg=state.name, align="center",
                 font=("Arial", 10, "normal"))


def main():
    states = extract_data()
    writer = get_writer()
    screen.setup(725, 491)
    screen.title("Name states")
    screen.bgpic("blank_states_img.gif")

    end_game = False
    max_num = len(states)
    correct_num = 0

    while not end_game:
        input_str = screen.textinput(
            title=f"{correct_num} / {max_num} correct states",
            prompt="Enter a valid US State :")
        for state in states:
            if state.name.lower() == \
                    input_str.strip().lower():
                correct_num += 1
                write(writer, state)
                states.remove(state)
                break
        if not len(states):
            end_game = True

    screen.exitonclick()


if __name__ == "__main__":
    main()
