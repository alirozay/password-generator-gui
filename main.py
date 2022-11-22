from tkinter import *
from tkinter import messagebox
import random
import json

LIGHT_BLUE = "#E8F9FD"
FONT = ('Cambria', 12, 'bold')
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LISTS = [SYMBOLS, NUMBERS, LOWER_CASE, UPPER_CASE]


# ---------------------------- PASSWORD GENERATOR
# ------------------------------- #
def password_generator() -> None:
    result = ""
    for i in range(15):
        password_entry.delete(0, END)
        list_choice = random.choice(LISTS)
        word = random.choice(list_choice)
        while True and i > 0:
            if result[i-1] in list_choice:
                list_choice = random.choice(LISTS)
                word = random.choice(list_choice)
            else:
                break
        result += word   #Check to see if previous symbol state matches the current symbol state
        password_entry.insert(END, string=result)


# ----------------------------- SEARCH PASSWOD -------------------------------#
def search_password() -> None:
    website = website_entry.get()
    try:
        with open(file="password.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Ops",
                             message="Password manager not initialized."
                                     "\nAdd a password to get started")
    else:
        try:
            data = data[website]
        except KeyError:
            messagebox.showerror(title="Ops", message="Password for "
                                                      "website not found")
        else:
            email = data["Email"]
            password = data["Password"]
            message = f"Email: {email}\nPassword: {password}"
            messagebox.showinfo(title="Details", message=message)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password() -> None:
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }
    if website != "" and email != "" and \
            password != 0:
        try:
            with open("password.json", mode='r') as f:
                data = json.load(f)
                data.update(new_data)

        except FileNotFoundError:
            with open("password.json", mode='w') as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("password.json", mode='w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="Please don't leave any "
                                                   "fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(background=LIGHT_BLUE)
window.minsize(width=400, height=300)

canvas = Canvas(width=200, height=225)
canvas.config(background=LIGHT_BLUE, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", bg=LIGHT_BLUE, font=FONT)
email_label = Label(text="Email/Username", bg=LIGHT_BLUE, font=FONT)
password_label = Label(text="Password", bg=LIGHT_BLUE, font=FONT)
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
email_entry.insert(END, string="alirozay@protonmail.com")
website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

add_button = Button(text="Add", width=36, command=save_password)
generate_button = Button(text="Generate", width=10, command=password_generator)
search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1)

window.mainloop()
