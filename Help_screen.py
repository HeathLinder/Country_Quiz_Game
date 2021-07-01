from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Help_Test:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = "aquamarine"

        # Help_Test Frame
        self.help_test_frame = Frame(width=300, height=300, bg=background_colour,
                                pady=10)
        self.help_test_frame.grid()

         # Help_Test Heading (row 0)
        self.help_test_label = Label(self.help_test_frame, text="Help Test",
                                font=("Oswald 19 bold"), bg=background_colour, 
                                padx=10, pady=10)
        self.help_test_label.grid(row=0)

        # Help/Rules Button (row 1)
        #self.help_and_rules_button = Button(self.help_test_frame, text="Help/Rules",
                                       # font="Oswald 15", bg="yellow", padx=10, pady=10)
       # self.help_and_rules_button.grid(row=1)






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Help/Rules")
    something = Help_Test(root)
    root.mainloop()
