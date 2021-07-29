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


        # Button Frame (row 2, three buttons inside frame)
        self.question_buttons_frame = Frame(self.start_screen_frame, bg=background_colour)
        self.question_buttons_frame.grid(row=2)

        # Buttons go here...
        button_font = "Oswald 10 bold"

        # 5 Question Button
        self.five_questions_button = Button(self.question_buttons_frame, text="5 Questions",
                                             font=button_font, bg="SpringGreen2")
        self.five_questions_button.grid(row=0, column=1, padx=5, pady=10)

        # 10 Question Button
        self.ten_questions_button = Button(self.question_buttons_frame, text="10 Questions",
                                            font=button_font, bg="DarkOrange1")
        self.ten_questions_button.grid(row=0, column=2, padx=5, pady=10)

        # 20 Question Button
        self.twenty_questions_button = Button(self.question_buttons_frame, text="20 Questions",
                                               font=button_font, bg="firebrick1")
        self.twenty_questions_button.grid(row=0, column=3, padx=5, pady=10)

        # Help & Game Statistics button (row 3, two buttons inside frame)
        self.help_and_statistics_buttons_frame = Frame(self.start_screen_frame, bg=background_colour)
        self.help_and_statistics_buttons_frame.grid(row=3)

        # Help & Game Statistics button 
        self.help_button = Button(self.help_and_statistics_buttons_frame, text="Help",
                                    bg="yellow", font="Oswald 15")
        self.help_button.grid(row=3, column=0, padx=5)

        self.game_statistics_button = Button(self.help_and_statistics_buttons_frame, 
                                            text="Game Statistics", 
                                            bg="snow4", font="Oswald 15")
        self.game_statistics_button.grid(row=3, column=1, padx=5)

    



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
