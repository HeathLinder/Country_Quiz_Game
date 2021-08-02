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
                                             font=button_font, bg="SpringGreen2", 
                                             command=self.play_screen)
        self.three_questions_button.grid(row=0, column=1, padx=5, pady=10)

        # 5 Question Button
        self.five_questions_button = Button(self.question_buttons_frame, text="5 Questions",
                                            font=button_font, bg="DarkOrange1", 
                                            command=self.play_screen)
        self.five_questions_button.grid(row=0, column=2, padx=5, pady=10)

        # 10 Question Button
        self.ten_questions_button = Button(self.question_buttons_frame, text="10 Questions",
                                               font=button_font, bg="firebrick1", 
                                               command=self.play_screen)
        self.ten_questions_button.grid(row=0, column=3, padx=5, pady=10)

    def play_screen(self):
        get_play_screen = Play_Screen(self)
        
        

class Play_Screen:
    def __init__(self, partner):

        # Disable the three question buttons after one is pushed
        partner.three_questions_button.config(state=DISABLED)
        partner.five_questions_button.config(state=DISABLED)
        partner.ten_questions_button.config(state=DISABLED)

        # Sets up the child window (ie: Play Box)
        self.play_box = Toplevel()

        # If user presses cross in top right, closes Play_Screen and re-enables question buttons
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play, partner))

        # Formatting Variables
        background_colour = "aquamarine"

        # Play Frame
        self.play_frame = Frame(self.play_box, width=300, height=300, bg=background_colour,
                                pady=10, padx=10)
        self.play_frame.grid()

        # Play Heading
        self.play_label = Label(self.play_frame, text="Country Quiz Game",
                                font=("Oswald 19 bold"), bg=background_colour,
                                padx=10, pady=10)
        self.play_label.grid(row=0)


    # Put help button back to normal...
    def close_play(self, partner):
        partner.three_questions_button.config(state=NORMAL)
        partner.five_questions_button.config(state=NORMAL)
        partner.ten_questions_button.config(state=NORMAL)
        self.play_box.destroy()




        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Welcome(root)
    root.mainloop()       