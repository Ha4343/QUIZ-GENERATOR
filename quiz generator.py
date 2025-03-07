import tkinter as tk
from tkinter import messagebox
import random
import time

# Questions database
questions = [
    {"question": "Which of the following is a mutable data type in Python?",
     "options": ["Tuple", "String", "List", "Integer"], "answer": "List"},
    {"question": "What is the time complexity of quicksort in the worst case?",
     "options": ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"], "answer": "O(n^2)"},
    {"question": "Which language is primarily used for Android development?",
     "options": ["Swift", "Java", "Kotlin", "C++"], "answer": "Kotlin"},
    {"question": "What does SQL stand for?",
     "options": ["Structured Query Language", "Sequential Query Language", "Standard Query Language", "Scripted Query Language"], "answer": "Structured Query Language"},
    {"question": "Which of these is NOT a JavaScript framework?",
     "options": ["React", "Angular", "Django", "Vue"], "answer": "Django"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Quiz App")
        self.root.geometry("500x400")
        
        self.score = 0
        self.current_question = 0
        self.time_left = 15
        
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 10))
            rb.pack(anchor="w")
            self.options.append(rb)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Arial", 10))
        self.timer_label.pack()
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 10))
        self.score_label.pack()
        
        self.next_question()

    def next_question(self):
        if self.current_question < len(questions):
            self.time_left = 15
            self.update_timer()
            q_data = questions[self.current_question]
            self.question_label.config(text=q_data["question"])
            self.var.set(None)
            
            for i in range(4):
                self.options[i].config(text=q_data["options"][i], value=q_data["options"][i])
        else:
            messagebox.showinfo("Quiz Complete", f"Your final score: {self.score}/{len(questions)}")
            self.root.quit()
    
    def check_answer(self):
        selected_answer = self.var.get()
        if selected_answer:
            correct_answer = questions[self.current_question]["answer"]
            if selected_answer == correct_answer:
                self.score += 1
            self.current_question += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.next_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer before submitting.")
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "You ran out of time!")
            self.current_question += 1
            self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
