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

        # Help/Rules Button (row 1)
        self.help_screen_button = Button(self.welcome_frame, text="Help",
                                        font="Oswald 15", bg="yellow", command=self.help_screen)
        self.help_screen_button.grid(row=1, padx=10, pady=10)

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
    root.title("Help")
    something = Welcome(root)
    root.mainloop()
