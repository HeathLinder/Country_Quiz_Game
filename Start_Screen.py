from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start_Screen:
    def __init__(self, parent):
        
        # Formatting Variables
        background_colour = "aquamarine"

        #  Start_Screen Frame
        self.start_screen_frame = Frame(height=200, width=400, pady=10, bg=background_colour)
        self.start_screen_frame.grid()

        # Main Heading (row 0)
        self.start_screen_label = Label(self.start_screen_frame, 
                                        text="Country Quiz Game", font="Oswald 19 bold", 
                                        bg=background_colour, padx=10, pady=10)
        self.start_screen_label.grid()

        # Instructions Label (row 1)
        self.instructions_label = Label(self.start_screen_frame, 
                                        text= "Please select the amount of questions " 
                                        "you would like to do, If you get stuck or don't " 
                                        "know how to play you can check the rules.", 
                                        font="Oswald 10 italic", wrap=300, 
                                        bg = background_colour, padx=10, pady=10)
        self.instructions_label.grid(row=1)


        # Button Frame (row 2)
        self.question_buttons_frame = Frame()
        self.question_buttons_frame.grid(row=2)

        # 5 Question Button

        # 10 Question Button

        # 20 Question Button

        # Help & Game Statistics Buttons (row 3, two buttons inside frame)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
