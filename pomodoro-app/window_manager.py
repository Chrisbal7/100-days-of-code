import tkinter as tk
from constants import *

window = tk.Tk()
window.title("POMODORO")
window.minsize(width=500, height=300)
window.configure(background=YELLOW)

tomato_img = tk.PhotoImage(file="tomato.png")
# Set up the tomato icon
tomato_icon = tk.PhotoImage(file="tomato-icon.png")
window.wm_iconphoto(True, tomato_icon)

# Center the app in the middle
main_frame = tk.Frame(window,
                      background=YELLOW,
                      padx=36,
                      pady=36)
main_frame.pack(expand=True)


def get_button(text="", font=(FONT_NAME, 13), bg=YELLOW):
    return tk.Button(main_frame, text=text,
                     font=font, bg=bg,
                     highlightthickness=False)


def get_label(text="", font=(FONT_NAME, 13), bg=YELLOW):
    return tk.Label(main_frame, text=text, font=font, bg=bg)


def get_canvas(img, text="00:00"):
    canvas = tk.Canvas(main_frame,
                       width=200,
                       height=224,
                       background=YELLOW,
                       borderwidth=0,
                       highlightthickness=False)
    canvas.create_image(100,
                        112,
                        image=img)
    text_ = canvas.create_text(100,
                               128,
                               text=text,
                               justify="center",
                               font=("Arial", 36),
                               fill="white")
    canvas.grid(row=1,
                column=1)
    return (canvas, text_)


def update_canvas_text(text="00:00"):
    global timer_canvas
    timer_canvas.itemconfig(canvas_text, text=text)


# Row 1
timer_label = get_label(text="Timer",
                        font=(FONT_NAME, 36), bg=YELLOW)
timer_label.config(fg=PINK)
timer_label.grid(row=0, column=1)

# Row 2
timer_canvas, canvas_text = get_canvas(tomato_img)
# Row 3
start_button = get_button(text="Start", bg=GREEN)
start_button.grid(row=2, column=2, sticky="E")

checkmark_label = get_label(font=("Arial", 16))
checkmark_label.config(fg=GREEN)
checkmark_label.grid(row=2, column=1)

reset_button = get_button(text="Reset", bg=RED)
reset_button.grid(row=2, column=0, sticky="W")
