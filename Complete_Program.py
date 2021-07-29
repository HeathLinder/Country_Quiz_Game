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
        self.help_screen_button = Button(self.help_and_statistics_buttons_frame, text="Help",
                                        font="Oswald 15", bg="yellow", command=self.help_screen)
        self.help_screen_button.grid(row=3, column=0, padx=5)

        self.game_statistics_button = Button(self.help_and_statistics_buttons_frame, 
                                            text="Game Statistics", 
                                            bg="snow4", font="Oswald 15")
        self.game_statistics_button.grid(row=3, column=1, padx=5)

    def help_screen(self):
        print("You asked for help.")
        get_help_screen = Help_Screen(self)
        
        

class Help_Screen:
    def __init__(self, partner):

        # Disable Help/Rules Button
        partner.help_screen_button.config(state=DISABLED)

        # Sets up the child window (ie: Help/Rules Box)
        self.help_box = Toplevel()

        # If user presses cross in top right, closes help and re-enables Help/Rules Button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Formatiing Variables
        background_colour ="aquamarine"

        # Help_Screen Frame
        self.help_screen_frame = Frame(self.help_box, width=250, height=300, bg=background_colour,
                                       pady=10, padx=10)
        self.help_screen_frame.grid()

        # Heading (row 0)
        self.help_screen_label = Label(self.help_screen_frame, text="Help",
                                        font="Oswald 19 bold", bg="aquamarine",
                                        padx=10, pady=10)
        self.help_screen_label.grid(row=0)

        # Instructions/Rules (row 1)
        self.help_screen_instructions = Label(self.help_screen_frame, text="Choose the amount of "
                                             "questions you would like to try out."
                                             "\nWhen you enter the play window,"
                                             " you will see an outline of a country and three buttons"
                                             " with three different country names."
                                             " Select one of these names and "
                                             "you will be told if it was correct or wrong"
                                             "and be moved on to the next question.\n"
                                             "Once the game is finished you will"
                                             "be able to choose the same amount or"
                                             "a different amount of question" 
                                             "if you wish to continue playing.",
                                             justify=LEFT, width=40, bg=background_colour, wrap=250)
        self.help_screen_instructions.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.help_screen_frame, text="Dismiss",
                                    width=10, bg="DeepSkyBlue2", 
                                    font="Oswald 19 bold", 
                                    command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)
        
        # Put help button back to normal...
    def close_help(self, partner):
        partner.help_screen_button.config(state=NORMAL)
        self.help_box.destroy()

        



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
