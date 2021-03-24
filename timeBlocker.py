# timeBlocker.py
# Date Created : March 23, 2021
# Original Author : Quinn Murphey (Nragis)
# GitHub Repo: https://www.github.com/Nragis/timeBlocker
# Thank You :)

import tkinter as tk
from tkinter import ttk
import os as os
import subprocess as sp
import random as random
import time as t
import datetime as dt

# Comments with increasing numbers of '#' preceding them indicates a comment hierarchy similar to MarkDown subtitles

colors = []
weekdays = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
months = ["NA", "January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Misc Functions

# This function gathers the possible color names for our Blocks
def read_color_file():
     with open("data/colors.cfg") as f:
         colors += f.readlines()

# Classes (Each class represents a container of some sort [Tk, TopLevel, Frame, Canvas, Menu])

# Main application. Creates main Toplevel widget that will contain a MainFrame
class TimeBlockerApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Time Blocker")

# Holds a ControlFrame and CanvasFrame
class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# Holds several buttons used to control the application
class ControlFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# Holds a canvas and two scrollbars for that canvas
class CanvasFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
# Holds TimerLabelFrame and BlockFrame and allows for both to be scrolled
class Canvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init(parent, *args, **kwargs)
        self.parent = parent

# Holds 24 labels representing each hour of the day. Each in a seperate row
class TimerLabelFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# Holds a variable number of BlockColumn frames
class BlockFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# Holds a variable number of Blocks
class BlockColumn(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# Holds a label and a checkbox
class Block(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

# A new window with all the application settings
class Settings(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

class Menu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

if __name__ == "__main__":
    root = TimeBlockerApplication()
    root.mainloop()
