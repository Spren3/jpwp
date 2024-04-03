import tkinter as tk
from tkinter import messagebox

class GridRowExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.buttons = []
        self.label = tk.Label(self, text="Numer przycisku:")
        self.label.grid(row=0, column=0, columnspan=3)
        button_width = 2  
        button_height = 2  

        for i in range(9):
            button = tk.Button(self, text=f'Przycisk {i}', width=button_width, height=button_height,
                               command=lambda i=i: self.buttonClicked(i))
            button.grid(row=1, column=i, padx=15, pady=10, sticky="nsew")  
            self.buttons.append(button)

        # Ustawianie rozciągliwej siatki
        for j in range(2):  
            self.grid_rowconfigure(j, weight=1)
        for i in range(9):  
            self.grid_columnconfigure(i, weight=1)

        self.geometry('400x300')
        self.title('Siatka TK - Rząd')

    def buttonClicked(self, i):
        button = self.buttons[i]
        button.config(text="Klik!")
        self.label.config(text=f"Numer przycisku: {i}")

if __name__ == '__main__':
    app = GridRowExample()
    app.mainloop()
