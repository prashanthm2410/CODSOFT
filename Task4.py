import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.choices = ['rock', 'paper', 'scissors']

        self.label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=5)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"

        messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
