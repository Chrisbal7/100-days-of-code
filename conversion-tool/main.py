""" This program converts miles to km,
using tkinter module for graphical user interface

by Chrisbal"""

import tkinter as tk

FONT = ("Arial", 13, "normal")
BACKGROUND = "white"
FOREGROUND = "#333"
MAIN_COLOR = "green"


def main(unit_1, unit_2, ratio):
    # Initialize a screen
    window = tk.Tk()
    window.title(f"{unit_1} to {unit_2} converter")
    window.config(background=BACKGROUND)

    def convert():
        try:
            unit_1_float = float(unit_1_var.get())
            unit_2_text = round(unit_1_float * ratio, 2)
        except ValueError:
            unit_2_text = "0"
        converted_unit.config(text=unit_2_text)

    def get_label(text=""):
        return tk.Label(main_frame,
                        justify="center",
                        text=text,
                        font=FONT,
                        background=BACKGROUND,
                        foreground=FOREGROUND)

    def get_entry(variable):
        return tk.Entry(main_frame,
                        justify="center",
                        textvariable=variable,
                        background=BACKGROUND,
                        foreground=FOREGROUND,
                        font=FONT,
                        width=8)

    def get_button(command, text=""):
        return tk.Button(main_frame, text=text,
                         bg=MAIN_COLOR,
                         fg=BACKGROUND,
                         font=FONT,
                         pady=6, relief="flat",
                         command=command)

    # variables
    unit_1_var = tk.StringVar()

    # mainframe
    main_frame = tk.Frame(window)
    main_frame.pack(expand=True)
    main_frame.configure(bg=BACKGROUND, padx=24, pady=24)
    # -----------------------------------------------------------
    unit_input = get_entry(unit_1_var)
    unit_input.grid(row=1, column=2)
    unit_1_label = get_label()
    unit_1_label.grid(row=1, column=3)
    # -----------------------------------------------------------------
    get_label(text="is equal to").grid(row=2, column=1)
    converted_unit = get_label()
    converted_unit.grid(row=2, column=2)
    get_label(unit_2).grid(row=2, column=3)
    # Button
    get_button(command=convert, text="Calculate").grid(row=3, column=2)
    # --------------------------------------------------------------------------
    window.mainloop()


if __name__ == "__main__":
    main("miles", "km", 1.602)
