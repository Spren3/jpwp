import tkinter as tk
from tkinter import messagebox

class GridColumnExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.buttons = []
        self.label = tk.Label(self, text="Numer przycisku:")
        self.label.grid(row=0, column=0, columnspan=3)
        button_width = 8  
        button_height = 2  

        for i in range(9):
            button = tk.Button(self, text=f'Przycisk {i}', width=button_width, height=button_height,
                               command=lambda i=i: self.buttonClicked(i))
            button.grid(row=i+1, column=0, padx=15, pady=10, sticky="nsew")  
            self.buttons.append(button)

        # Ustawianie rozciągliwej siatki
        for i in range(10): 
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.geometry('300x400')
        self.title('Siatka TK - Kolumna')

    def buttonClicked(self, i):
        button = self.buttons[i]
        button.config(text="Klik!")
        self.label.config(text=f"Numer przycisku: {i}")

if __name__ == '__main__':
    app = GridColumnExample()
    app.mainloop()
