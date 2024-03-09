import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("200x150")
root.configure(bg="#1C1C1C")

def shorten():
    shortener = pyshorteners.Shortener()
    shortUrl = shortener.tinyurl.short(orjUrlEntry.get())
    shortUrlEntry.delete(0, tkinter.END)
    shortUrlEntry.insert(0, shortUrl)

orjUrlLabel = tkinter.Label(root, text="Enter your URL", bg="#1C1C1C", fg="white")
orjUrlEntry = tkinter.Entry(root, bg="#1C1C1C", fg="white")
shortUrlLabel = tkinter.Label(root, text="Shortened URL", bg="#1C1C1C", fg="white")
shortUrlEntry = tkinter.Entry(root, bg="#1C1C1C", fg="white")
shortUrlButton = tkinter.Button(root, text="Shorten URL!", command=shorten, bg="white", fg="black")

orjUrlLabel.pack()
orjUrlEntry.pack()
shortUrlLabel.pack()
shortUrlEntry.pack()
shortUrlButton.pack()

root.mainloop()
