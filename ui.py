from tkinter import *
from my_data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
WIDTH = 300 + 20
HEIGHT = 250 + 20

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):


        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score = Label(
            text="Score: 0",
            fg="white",
            background=THEME_COLOR
        )
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Also Works!
        # self.label = Canvas(width = 300,height= 250,bg = "white")
        # self.question_text = self.label.create_text(150, 125, text="Some text", fill = THEME_COLOR)
        # self.label.grid(row=1, column=0, columnspan=2)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The party is over. Go home.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)





