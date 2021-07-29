from tkinter import *
from functools import partial # To prevent unwanted windows
import random

class Welcome:
    def __init__(self, parent):

        # Formatting Variables
        background_colour = "aquamarine"

        # Welcome Frame
        self.welcome_frame = Frame(width=300, height=300, bg=background_colour,
                                pady=10, padx=10)
        self.welcome_frame.grid()

         # Welcome Heading (row 0)
        self.welcome_label = Label(self.welcome_frame, text="Welcome",
                                    font=("Oswald 19 bold"), bg=background_colour, 
                                    padx=10, pady=10)
        self.welcome_label.grid(row=0)

        # Button Frame (row 2, three buttons inside frame)
        self.question_buttons_frame = Frame(self.welcome_frame, bg=background_colour)
        self.question_buttons_frame.grid(row=2)

        # Buttons go here...
        button_font = "Oswald 10 bold"

        # 3 Question Button
        self.three_questions_button = Button(self.question_buttons_frame, text="3 Questions",
                                             font=button_font, bg="SpringGreen2")
        self.three_questions_button.grid(row=0, column=1, padx=5, pady=10)

        # 5 Question Button
        self.five_questions_button = Button(self.question_buttons_frame, text="5 Questions",
                                            font=button_font, bg="DarkOrange1")
        self.five_questions_button.grid(row=0, column=2, padx=5, pady=10)

        # 10 Question Button
        self.ten_questions_button = Button(self.question_buttons_frame, text="10 Questions",
                                               font=button_font, bg="firebrick1")
        self.ten_questions_button.grid(row=0, column=3, padx=5, pady=10)

        

        

        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Welcome(root)
    root.mainloop()       