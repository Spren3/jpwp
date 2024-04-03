import tkinter as tk
from tkinter import messagebox

class GridExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.buttons = []
        self.label = tk.Label(self, text="Numer przycisku: -")
        self.label.grid(row=0, column=0, columnspan=3)
        button_width = 8  # Stała szerokość przycisku
        button_height = 2  # Stała wysokość przycisku

        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text=f'Przycisk {i},{j}', width=button_width, height=button_height,
                                   command=lambda i=i, j=j: self.buttonClicked(i, j))
                button.grid(row=i+1, column=j, padx=15, pady=10, sticky="nsew")  # Zmniejszenie odstępów między przyciskami
                self.buttons.append(button)

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        self.geometry('300x200')
        self.title('Siatka TK')

    def buttonClicked(self, i, j):
        button = self.buttons[i*3 + j]
        button.config(text="Kliknięte!")
        self.label.config(text=f"Numer przycisku: {i*3 + j}")

if __name__ == '__main__':
    app = GridExample()
    app.mainloop()
