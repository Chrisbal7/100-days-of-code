from window_manager import *
from tkinter import messagebox

import csv
import random

current_card = {}

with open("data/french_words.csv") as csv_file:
    words = list(csv.DictReader(csv_file))


def update_card(language, word, image, fg="black"):
    card_canvas.itemconfig(card_img, image=image)
    card_canvas.itemconfig(card_lang_text, text=language, fill=fg)
    card_canvas.itemconfig(card_word, text=word, fill=fg)
    window.update()


def next_card():
    global current_card, flip_timer
    current_card = get_word()
    try:
        update_card("French", current_card["French"],
                    front_card_image)
    except TypeError:
        messagebox.showerror(title="Oops",
                             message="Something went wrong, \n"
                                     "Please refresh the app")
        exit()
    else:
        flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    global current_card
    update_card("English", current_card["English"],
                back_card_image, fg="white")


def main():
    next_card()
    right_btn.config(command=is_known)
    wrong_btn.config(command=next_card)


def get_word():
    if len(words):
        return random.choice(words)


def is_known():
    global current_card, words
    words.remove(current_card)
    next_card()


flip_timer = window.after(ms=3000, func=flip_card)
main()
window.mainloop()
