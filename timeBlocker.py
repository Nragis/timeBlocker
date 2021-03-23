from tkinter import *
from tkinter import ttk
import os as os
import subprocess as sp
import random as random
import time as t

colors = []

def read_color_file():
    with open("data/colors.cfg") as f:
        colors += f.readlines()

def play_sound(fileName):
    basePath = os.getcwd()
    sp.Popen(['play', '{}/sounds/{}'.format(basePath, fileName)])

class pomodoro:
    def __init__(self, parent):
        # Initializing Variables

        # Initializing mainframe and title
        self.parent = parent
        root.title("Time Blocker")

        # Initializing Styles
        
        # Creating mainframe
        self.mainframe = ttk.Frame(parent)

        # Creating and placing containers

        # Creating and placing timerFrame widgets

        # Creating and placing taskFrame widgets
        
        # Creating and placing doneFrame widgets
       
        # row/column configure

        # Bind keys

    def open_settings(self):
        pass

if __name__ == "__main__":
    root = Tk()
    timeBlock(root)
    root.mainloop()
