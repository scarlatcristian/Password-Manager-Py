from tkinter import *

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
btn_generate_password = Button(text="Generate Password", width=11)
btn_generate_password.grid(row=3, column=2)

btn_add = Button(text="Add", width=34)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
