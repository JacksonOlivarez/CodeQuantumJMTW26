import tkinter as tk
from tkinter import ttk
import csv
# names, teams from file
lapFile = 'CSVFiles/LapTimes.csv'
resultsFile = 'CSVFiles/RaceResults.csv' # contains team names,
columns = []
rows = []

with open(resultsFile, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for columns in csvreader:
        print(columns)
        columns.append(columns)

class F1driver:
    def __init__(self, name, team, teamcolor):
        self.name = name
        self.team = team
        self.teamcolor = teamcolor

    def __repr__(self):
        return f"{self.name} | Team: {self.team} | Teamcolor: {self.teamcolor}"

class F1Database:
    def __init__(self, csv_file):
        self.drivers = []
        self.loadCsv(csv_file)


print("Columns: " + str(len(columns)))
# This is how we comment
'''if (__name__ == "__main__"):
    frame = tk.Tk()

    frame.geometry("1000x1000")
    frame.title("Code Quantum Project")

    label = tk.Label(frame, text="What's up", font=("Arial", 18))
    label.pack(anchor="n", pady=450)

    combo_box = ttk.Combobox(
        frame,
        values=["2024", "2025", "2026"],
        state="readonly"
    )
    combo_box.place(relx=0.5, rely=0.5, anchor="center")
    print(combo_box.get())

    combo_box.set("Option 1")
    frame.mainloop()
'''
