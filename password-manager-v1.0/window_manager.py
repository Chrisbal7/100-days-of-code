import tkinter as tk

BACKGROUND = "white"
FONT = ("Courier", 13)
FOREGROUND = "#333"

window = tk.Tk()
window.title("PASSWORD MANAGER")
window.minsize(width=500, height=300)
window.configure(background=BACKGROUND)

# Set up the tomato icon
icon = tk.PhotoImage(file="logo.png")
window.wm_iconphoto(True, icon)

# Center the app in the middle
main_frame = tk.Frame(window,
                      background=BACKGROUND,
                      padx=36,
                      pady=36)
main_frame.pack(expand=True)


def clear_entry(entry):
    entry.delete(0, tk.constants.END)


def get_button(row, col, text="", font=FONT, bg=BACKGROUND):
    button = tk.Button(main_frame, text=text,
                       font=font, bg=bg,
                       fg=FOREGROUND,
                       highlightthickness=False)
    button.grid(row=row, column=col)
    return button


def get_input(text, variable, row, sticky=True):
    get_label(text=text).grid(row=row, column=0)
    entry = get_entry(variable)
    entry.grid(row=row, column=1)
    if sticky:
        entry.grid(columnspan=2, sticky=("W", "E"))
    else:
        entry.grid(sticky="W")
    return entry


def get_label(text="", font=FONT, bg=BACKGROUND):
    return tk.Label(main_frame,
                    text=text, font=font,
                    fg=FOREGROUND,
                    bg=bg,
                    pady=8)


def get_entry(variable):
    return tk.Entry(main_frame,
                    textvariable=variable,
                    highlightthickness=False,
                    bg=BACKGROUND,
                    fg=FOREGROUND)


def get_canvas(row, col, img):
    canvas = tk.Canvas(main_frame,
                       width=200,
                       height=190,
                       background=BACKGROUND,
                       borderwidth=0,
                       highlightthickness=False)
    canvas.create_image(100,
                        112,
                        image=img)
    canvas.grid(row=row, column=col)
    return canvas


website_var = tk.StringVar()
username_var = tk.StringVar()
password_var = tk.StringVar()

image = tk.PhotoImage(file="logo.png")
# Row 1
logo_canvas = get_canvas(0, 1, image)

website_input = get_input("Website: ", website_var, 1, sticky=False)
search_btn = get_button(1, 2, text="Search", bg="blue")
user_input = get_input("Username/Email: ", username_var, 2)
password_input = get_input("Password: ", password_var, 3, sticky=False)

user_input.insert(0, "chrisbal@gmail.com")

generate_btn = get_button(3, 2, text="Generate", bg="green")
add_btn = get_button(4, 1, text="Add", bg="Blue")
add_btn.grid(columnspan=2, sticky=("W", "E"))
