from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start_Screen:
    def __init__(self, parent):
        
        # Formatting Variables
        background_colour = "aquamarine"

        # Frame
        self.start_screen_frame = Frame(height=200, width=400, pady=10, bg=background_colour)
        self.start_screen_frame.grid()

        # Main Heading (row 0)
        self.start_screen_label = Label(self.start_screen_frame, text="Country Quiz Game", font="Oswald 19 bold", bg=background_colour, padx=10, pady=10)
        self.start_screen_label.grid()

        # Instructions Label (row 1)

        # Question Buttons (row 2, three buttons inside frame)

        # Help & Game Statistics Buttons (row 3, two buttons inside frame)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
