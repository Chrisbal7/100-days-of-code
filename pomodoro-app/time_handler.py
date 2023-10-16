""" This module implements methods relative to the timer
such as initial time, timer count_down, reset the timing"""
from time import sleep
from window_manager import *


class Timer:
    def __init__(self, initial_value, state, color):
        self.initial_value = initial_value
        self.time = initial_value
        self.screen = window
        self.state = state
        self.color = color
        self.is_reset = False

    def count_down(self):
        timer_label.config(text=self.state, fg=self.color)

        while self.time and not self.is_reset:
            sleep(0.978)
            self.time -= 1
            self.update()
            reset_button.configure(command=
                                   lambda: self.reset(start_button))

    def refresh(self):
        self.screen.update()
        minutes = self.time // 60
        seconds = self.time % 60
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        return f"{minutes}:{seconds}"

    def reset(self, button):
        self.time = 0
        timer_label.config(text="Timer")
        button.config(state="active")
        self.update()
        self.is_reset = True
        checkmark_label.config(text="")

    def update(self):
        update_canvas_text(self.refresh())

    def restore(self):
        self.time = self.initial_value
        self.is_reset = False
