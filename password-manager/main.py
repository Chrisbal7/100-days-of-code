# import pyperclip
import random
from tkinter import messagebox

from window_manager import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_+{}:"|<>?~`-=[];\\,./\''
all_char = numbers + letters + symbols


def generate_password():
    length = random.randint(8, 16)
    password_generated = ""
    for _ in range(length):
        password_generated += random.choice(all_char)
    password_var.set(password_generated)
    # pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_var.get()
    user = username_var.get()
    password = password_var.get()
    all_values = [website, user, password]
    if website and user and password:
        permission = messagebox.askyesno(title=website,
                                         message=f"Are you sure to save {user}?",
                                         icon="question")
        if permission:
            with open("data.txt", "a") as file:
                file.write(" | ".join(all_values) + "\n")
            messagebox.showinfo(title="Result", message="Successfully saved!")
            for entry in [password_input, user_input, website_input]:
                clear_entry(entry)
    else:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty!")


# ---------------------------- UI SETUP ------------------------------- #
generate_btn.config(command=generate_password)
add_btn.config(command=save_password)

window.mainloop()
