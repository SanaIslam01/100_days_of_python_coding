import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = ["What is the capital of France?", "Who is the author of 'Harry Potter' series?", "What is the chemical symbol for water?"]
        self.answers = ["Paris", "J.K. Rowling", "H2O"]
        self.current_question_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index])
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            self.root.destroy()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.answers[self.current_question_index]

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")

        self.current_question_index += 1
        self.answer_entry.delete(0, tk.END)
        self.display_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
