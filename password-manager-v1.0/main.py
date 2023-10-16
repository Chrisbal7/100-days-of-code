# import pyperclip
import random
import json

from tkinter import messagebox
from window_manager import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_+{}:"|<>?~`-=[];\\,./\''
all_char = numbers + letters + symbols


def get_values_from_input():
    return (website_var.get(),
            username_var.get(),
            password_var.get())


def get_password_list():
    try:
        with open("data.json") as file_obj:
            password_list = json.load(file_obj)
    except FileNotFoundError:
        password_list = []
    return password_list


def search():
    website_q, user_q, passwd = get_values_from_input()
    password_list = get_password_list()
    for credential in password_list:
        if credential.get("website") == website_q.strip():
            if credential.get("user") == user_q.strip():
                messagebox.showinfo(title=website_q,
                                    message=f"Username:{credential.get('user')}\n"
                                            f"Password: {credential.get('password')}")
                return True
    messagebox.showerror(title="Password manager",
                         message="Oops! \nIncorrect website or Username!")


def generate_password():
    length = random.randint(8, 16)
    password_generated = ""
    for _ in range(length):
        password_generated += random.choice(all_char)
    password_var.set(password_generated)
    # pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website, user, password = get_values_from_input()
    credential = {"website": website, "user": user, "password": password}
    if website and user and password:
        permission = messagebox.askyesno(title=website,
                                         message=f"Are you sure to save {user}?",
                                         icon="question")
        if permission:
            data = get_password_list()
            data.append(credential)
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
            messagebox.showinfo(title="Result", message="Successfully saved!")
            for entry in [password_input, user_input, website_input]:
                clear_entry(entry)
    else:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty!")


# ---------------------------- UI SETUP ------------------------------- #
generate_btn.config(command=generate_password)
add_btn.config(command=save_password)
search_btn.config(command=search)

window.bind("<Return>", func=lambda e: save_password())
window.mainloop()
