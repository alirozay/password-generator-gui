from tkinter import *
from tkinter import messagebox
import random

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
    password_entry.delete(0, END)
    for i in range(15):
        list_choice = random.choice(LISTS)
        result += random.choice(list_choice)
        password_entry.insert(END, string=result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password() -> None:
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website != "" and email != "" and \
            password != 0:
        result = f"{website} | {email} | {password}"
        with open("password.txt", mode='a+') as f:
            f.seek(0)
            passwords = f.readlines()
            for i in range(len(passwords)):
                passwords[i] = passwords[i].strip()
            if result not in passwords:
                is_ok = messagebox.askokcancel(title="Save password?",
                                               message=f"These are the details:\n"
                                                       f"Website: {website}\n"
                                                       f"Email: {email}\n"
                                                       f"Password: {password}")
                if is_ok:
                    f.seek(0, 2)
                    f.write(f"{result}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
            else:
                messagebox.showerror(title="Oops", message="Password already "
                                                           "exists")
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
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1)

window.mainloop()
