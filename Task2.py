import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, textvariable=self.result_var, width=20, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, column) in self.buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

        self.clear_button = tk.Button(self.root, text='C', width=5, height=2, command=self.clear_entry)
        self.clear_button.grid(row=5, column=0, columnspan=4, sticky='nsew')

        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = str(eval(expression))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

    def clear_entry(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
