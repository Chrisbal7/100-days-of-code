import tkinter as tk

BACKGROUND = "#B1DDC6"
FOREGROUND = "#333"


def get_canvas(row, col):
    canvas = tk.Canvas(main_frame,
                       width=800,
                       height=526,
                       background=BACKGROUND,
                       borderwidth=0,
                       highlightthickness=False)
    canvas.grid(row=row, column=col, columnspan=4)
    img = canvas.create_image(400, 250, image=front_card_image)
    lang_text = canvas.create_text(400, 183, text="",
                                   font=("Arial", 24, "italic"), fill=FOREGROUND)
    word = canvas.create_text(400, 268, text="",
                              font=("Arial", 36, "bold"), fill=FOREGROUND)
    return (canvas, img, lang_text, word)


def get_button(row, col, img, sticky):
    button = tk.Button(main_frame, image=img,
                       fg=FOREGROUND,
                       highlightthickness=False, relief="flat")
    button.grid(row=row, column=col, sticky=sticky)
    return button


def get_photo_image(path):
    return tk.PhotoImage(file=path)


#  UI SETUP
window = tk.Tk()
window.title("FLASH CARDS")
window.minsize(width=500, height=300)
window.configure(background=BACKGROUND)

# Images
icon = get_photo_image("images/right.png")
right_image = get_photo_image("images/right.png")
wrong_image = get_photo_image("images/wrong.png")
front_card_image = get_photo_image("images/card_front.png")
back_card_image = get_photo_image("images/card_back.png")

window.wm_iconphoto(True, icon)

# Center the app in the middle
main_frame = tk.Frame(window, background=BACKGROUND, padx=36,
                      pady=36)
main_frame.pack(expand=True)

card_canvas, card_img, \
    card_lang_text, card_word = get_canvas(0, 0)
wrong_btn = get_button(1, 1, wrong_image, "W")
right_btn = get_button(1, 2, right_image, "E")
