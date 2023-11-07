import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


def generate_password():
    entry_password.delete(0, END)
    letters = "abcdefghijklmnopqrstvwxqz" + "abcdefghijklmnopqrstvwxqz".upper()
    symbols = "!@#$%^&*?()+"
    numbers = '1234567890'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password = password_letters + password_number + password_symbols

    shuffle(password)
    password = "".join(password)
    entry_password.insert(0, f"{password}")


def save_data():
    website_name = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website_name == "" or email == "" or password == "":
        messagebox.showwarning(
            title="Empty field", message="All fields must be completed before saving")
    else:
        save_info = messagebox.askokcancel(
            title=website_name, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if save_info:
            with open("./data.txt", "a") as file:
                file.write(
                    f"Name: {website_name} | Email: {email} | Password: {password}\n")

            pyperclip.copy(password)
            entry_website.delete("0", END)
            entry_password.delete("0", END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=180, height=200)
lock_image = PhotoImage(file="./lock.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Inputs
entry_website = Entry(width=36)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

entry_email = Entry(width=36)
entry_email.insert(0, "test@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

# Button
btn_generate_password = Button(
    text="Generate Password", width=11, command=generate_password)
btn_generate_password.grid(row=3, column=2)

btn_add = Button(text="Add", width=34, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
