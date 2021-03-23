from tkinter import *
from tkinter import ttk
import os as os
import subprocess as sp
import random as random
import time as t
import datetime as dt

colors = []
weekdays = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
months = ["NA", "January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def read_color_file():
    with open("data/colors.cfg") as f:
        colors += f.readlines()

def play_sound(fileName):
    basePath = os.getcwd()
    sp.Popen(['play', '{}/sounds/{}'.format(basePath, fileName)])

class timeBlock:
    def __init__(self, Parent):
        # Initializing Variables
        self.date = dt.date.today()

        # Initializing MainFrame and title
        self.Parent = Parent
        self.Parent.title("Time Blocker")

        # Initializing Styles
        
        # Creating MainFrame
        self.MainFrame = ttk.Frame(self.Parent)
        self.MainFrame.grid(row=0, column=0, sticky="N E S W")

        # Creating and placing containers
        self.TopFrame = ttk.Frame(self.MainFrame)
        self.BottomFrame = ttk.Frame(self.MainFrame)
       
        self.TopFrame.grid(row=0,column=0,sticky="N E S W")
        self.BottomFrame.grid(row=1,column=0,sticky="N E S W")

        # Creating and placing TopFrame widgets
        self.DateStringVar = StringVar()
        self.update_date_string()

        self.SettingsButton = ttk.Button(self.TopFrame, style="SettingsButton.TopFrame.TButton", text="Settings", command=self.open_settings)
        self.LeftDateButton = ttk.Button(self.TopFrame, style="LeftDateButton.TopFrame.TButton", text="<", command = lambda newDate=self.date - dt.timedelta(days=1): self.change_date(newDate))
        self.CurrentDateButton = ttk.Button(self.TopFrame, style="CurrentDateButton.TopFrame.TButton", textvariable=self.DateStringVar, command=self.open_date_menu)
        self.RightDateButton = ttk.Button(self.TopFrame, style="RightDateButton.TopFrame.TButton", text=">", command = lambda newDate=self.date + dt.timedelta(days=1): self.change_date(newDate))

        self.SettingsButton.grid(row=0,column=0,sticky = "N W")
        self.LeftDateButton.grid(row=0, column=1, sticky = "E")
        self.CurrentDateButton.grid(row=0,column=2, sticky= "")
        self.RightDateButton.grid(row=0, column=3, sticky= "W")

        # Creating and placing BottomFrame widgets

        # row/column configure
        self.Parent.rowconfigure(0, weight=1)
        self.Parent.columnconfigure(0, weight=1)

        self.MainFrame.rowconfigure(0, weight=0, minsize=100)
        self.MainFrame.rowconfigure(1, weight=1, minsize=1000)
        self.MainFrame.columnconfigure(0, weight=1, minsize=800)

        self.TopFrame.columnconfigure(0, weight=0, minsize = 100)
        self.TopFrame.columnconfigure(1, weight=1)
        self.TopFrame.columnconfigure(2, weight=0)
        self.TopFrame.columnconfigure(3, weight=1)
        self.TopFrame.columnconfigure(4, weight=0, minsize = 100)

        # Bind keys

    def open_settings(self):
        pass

    def change_date(self, newDate):
        pass

    def open_date_menu(self):
        pass

    def update_date_string(self):
        self.DateStringVar.set(weekdays[self.date.weekday()] + ", " + months[self.date.month] + " " + str(self.date.day))

if __name__ == "__main__":
    root = Tk()
    timeBlock(root)
    root.mainloop()
