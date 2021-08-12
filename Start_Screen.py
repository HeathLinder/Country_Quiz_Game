from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start_Screen:
    def __init__(self, parent):

        # Set Initial questions to zero
        self.input_questions= IntVar()
        self.input_questions.set(0)
        
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
                                        text= "Please enter the amount of questions " 
                                        "you would like to do out of 3,5,10. " 
                                        "Then click the 'Add Questions button,"
                                        "and choose your question amount that you entered!", 
                                        font="Oswald 10 italic", wrap=300, 
                                        bg = background_colour, padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Input box, Button & Error Label (row 2)
        self.input_error_frame = Frame(self.start_screen_frame, width=200)
        self.input_error_frame.grid(row=2)

        self.questions_amount_entry = Entry(self.input_error_frame,
                                            font="Oswald 19 bold", width=10)
        self.questions_amount_entry.grid(row=0, column=0)

        self.add_questions_button = Button(self.input_error_frame,
                                           font="Oswalad 14 bold",
                                           text="Add Questions",
                                           command=self.check_questions)
        self.add_questions_button.grid(row=0, column=1)

        self.questions_error_label = Label(self.input_error_frame,
                                           bg=background_colour, text="",
                                           font="Oswald 10 bold", wrap=270,
                                           justify=LEFT)
        self.questions_error_label.grid(row=1, columnspan=2, pady=5)



        # Button Frame (row 3, three buttons inside frame)
        self.question_buttons_frame = Frame(self.start_screen_frame, bg=background_colour)
        self.question_buttons_frame.grid(row=3)

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

        # Diable all buttons at start
        self.three_questions_button.config(state=DISABLED)
        self.five_questions_button.config(state=DISABLED)
        self.ten_questions_button.config(state=DISABLED)

        # Help & Game Statistics button (row 4, two buttons inside frame)
        self.help_and_statistics_buttons_frame = Frame(self.start_screen_frame, bg=background_colour)
        self.help_and_statistics_buttons_frame.grid(row=4)

        # Help & Game Statistics button 
        self.help_button = Button(self.help_and_statistics_buttons_frame, text="Help",
                                    bg="yellow", font="Oswald 15")
        self.help_button.grid(row=4, column=0, padx=5)

        self.game_statistics_button = Button(self.help_and_statistics_buttons_frame, 
                                            text="Game Statistics", 
                                            bg="snow4", font="Oswald 15")
        self.game_statistics_button.grid(row=4, column=1, padx=5)
    
    def check_questions(self):
        starting_questions = self.questions_amount_entry.get()

        # Set error background colours (and assume that there are no)
        # errors at the start)
        error_back = "ffafaf"
        has_errors = "no"

        # Diable all question buttons in case user changes
        # mind and decreases amount entered.
        self.three_questions_button.config(state=DISABLED)
        self.five_questions_button.config(state=DISABLED)
        self.ten_questions_button.config(state=DISABLED)

        try:
            starting_questions = int(starting_questions)

            if starting_questions < 3:
                has_errors = "yes"
                error_feedback = "Sorry, the least amount you can play is 3 questions"
            elif starting_questions > 10:
                has_errors = "yes"
                error_feedback = "Too high! The most amount of questions you " \
                                 "can play is 10"

            elif starting_questions == 10:
                # enable ten questions button
                self.ten_questions_button.config(state=NORMAL)
            elif starting_questions == 5:
                # enable five questions button
                self.five_questions_button.config(state=NORMAL)
            elif starting_questions == 3:
                # enable three questions button
                self.three_questions_button.config(state=NORMAL)
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a question amount (no text / decimals)"

        if has_errors == "Yes":
            self.questions_amount_entry.config(bg=error_back)
            self.questions_error_label.config(text=error_feedback)
        else:
            # set starting balance to amount enterted by user
            self.input_questions.set(starting_questions)

    def to_game(self, questions):

        # retrive starting questions
        starting_amount = self.input_questions.get()

        game(self, questions, starting_amount)

        # hide start up window
        root.withdraw()

class Play_Screen:
    def __init(self, partner, questions, starting_amount):
        print(questions)
        print(starting_amount)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz Game")
    something = Start_Screen(root)
    root.mainloop()
