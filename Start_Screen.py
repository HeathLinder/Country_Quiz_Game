from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start_Screen:
    def __init__(self, parent):
        print("Hello World")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
