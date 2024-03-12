import tkinter
from tkinter import messagebox

def leapYearCheck():
    if (int(yearEntry.get()) % 4 == 0 and (int(yearEntry.get()) % 100 != 0 or (int(yearEntry.get()) % 400 == 0))):

        messagebox.showinfo(title="Leap Year", message=(str(yearEntry.get()) + " is a leap year!"))
    else:
        messagebox.showinfo(title="Leap Year", message=(str(yearEntry.get()) + " is NOT a leap year!"))


# Frame
root = tkinter.Tk()
root.title("Check Leap Year")
root.geometry("250x150")
root.configure(bg="#1C1C1C")

# Widgets
yearLabel = tkinter.Label(root, text="Enter a year: ", bg="#1C1C1C", fg="white", font=("Helvetica", 20))
yearEntry = tkinter.Entry(root, bg="#1C1C1C", fg="white", font=("Helvetica", 15))
yearButton = tkinter.Button(root, text="Check!", command=leapYearCheck, bg="#1C1C1C", fg="white", font=("Helvetica", 20))

# Positioning
yearLabel.pack()
yearEntry.pack()
yearButton.pack()

root.mainloop()