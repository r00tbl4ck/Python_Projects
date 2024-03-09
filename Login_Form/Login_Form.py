import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry("500x500")
window.configure(bg="#1C1C1C")

frame = tkinter.Frame(bg="#1C1C1C")

def login():
    username = "admin"
    password = "Pa$$w0rd!"
    if usernameEntry.get() == username and passwordEntry.get() == password:
        messagebox.showinfo(title="Success!", message="Welcome back " + username + "!")
    else:
        messagebox.showinfo(title="Invalid Login!", message="Invalid username or password!")

# Creating widgets
loginLabel = tkinter.Label(frame, text="Login", bg="#1C1C1C", fg="#2F9DFF", font=("Monospace", 16, "bold"))
usernameLabel = tkinter.Label(frame, text="Username", bg="#1C1C1C", fg="white", font=("Open Sans Light", 10))
passwordLabel = tkinter.Label(frame, text="Password", bg="#1C1C1C", fg="white", font=("Open Sans Light", 10))
usernameEntry = tkinter.Entry(frame, font=("Open Sans Light", 10))
passwordEntry = tkinter.Entry(frame, show="*", font=("Open Sans Light", 10))
loginButton = tkinter.Button(frame, text="Login", bg="#2F9DFF", fg="#FFFFFF", font=("Monospace", 10, "bold"), command=login)

# Placing widgets on the screen
frame.pack()
loginLabel.grid(row=0, column=1, columnspan=1, sticky="news", pady=20)
usernameLabel.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0, pady=5)
passwordEntry.grid(row=2, column=1, pady=5)
loginButton.grid(row=3, column=1, columnspan=1, pady=10)

window.mainloop()