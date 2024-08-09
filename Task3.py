import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Generated Password:")
        self.result_label.pack(pady=5)

        self.password_display = tk.Entry(root, width=40)
        self.password_display.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive.")
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
        except ValueError:
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "Invalid length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
