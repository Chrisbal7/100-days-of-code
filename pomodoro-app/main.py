""" The pomodoro technique for productivity
incorporated into an app"""

from window_manager import *
from time_handler import Timer
from constants import *

work_timer = Timer(WORK_TIME, "Work Time", RED)
rest_timer = Timer(SHORT_BREAK_TIME, "Break Time", PINK)
long_break = Timer(LONG_BREAK_TIME, "Break Time", GREEN)

timers = [work_timer, rest_timer, long_break]


def main():
    check_mark = ""
    i = 4
    while i > 0:
        for timer in timers:
            if timers[-1] == timer and i != 1:
                continue
            start_count(timer)
            if timer.is_reset:
                return False
        check_mark += "✔"
        checkmark_label.config(text=check_mark)
        i -= 1


def start_count(timer):
    start_button.configure(state="disabled")
    timer.restore()
    timer.count_down()


# start button command
start_button.config(command=main)
window.bind("<Return>", lambda e: main)
window.mainloop()
