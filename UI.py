import tkinter as tk
from tkinter import *

from main import columns


def selection(event):
    userYear = event.widget.get()
    print("Year: " + userYear)





if (__name__ == "__main__"):
    frame = tk.Tk()
    mainPage = Frame(frame)
    driverPage = Frame(frame)



    frame.geometry("1000x1000")
    frame.title("Code Quantum Project")

    mainPage.grid(row=0, column=0, sticky="nsew")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    container = Frame(mainPage)
    container.place(relx=0.5, rely=0.5, anchor="center")

    label = tk.Label(mainPage, text="F1 Data Manager", font=("Arial", 18))
    label.pack(padanchor="center")

    driverBut = Button(mainPage, text="Open", command=lambda: driverPage.tkraise())
    driverBut.pack(pady=0)

    frame.mainloop()


class driverPage:
    # Include Track Picture
    # Name, Team Name, Car Info, Pit Info,
    # Headshot
    def __init__(self, master):
        image = PhotoImage(file="Media/DriverHeadshots/LewisHamilton.png")



