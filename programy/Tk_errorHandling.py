import tkinter as tk
from tkinter import messagebox

class ErrorHandlingExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.title("Obsługa błędu w Tkinter")
        self.geometry("300x200")

        button1 = tk.Button(self, text="rzuć błąd valueError", command=self.generateError)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Obsługa błędu dzielenia", command=self.divideByZero)
        button2.pack(pady=10)

    def generateError(self):
        try:
            # rzucamy jakis błąd ręcznie
            raise ValueError("Przykładowy błąd")

        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

    def divideByZero(self):
        try:
            result = 1 / 0  # Dzielenie przez zero
            messagebox.showinfo("Wynik", f"Wynik: {result}")

        except ZeroDivisionError as e:
            messagebox.showerror("Błąd", f"Podzieliłeś przez zero: {str(e)}")

if __name__ == '__main__':
    app = ErrorHandlingExample()
    app.mainloop()
