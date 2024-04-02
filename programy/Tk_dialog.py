import tkinter as tk
from tkinter import simpledialog, messagebox

class DialogExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.title("Okienko dialogowe Tkinter")
        self.geometry("300x200")

        button1 = tk.Button(self, text="Otworz aby wpisać", command=self.openSimpleDialog)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Kliknij aby zobaczyć wiadomość dla ciebie", command=self.openMessageBox)
        button2.pack(pady=10)

    def openSimpleDialog(self):
        result = simpledialog.askinteger("Okienko do wpisania", "Wpisz liczbę:")
        if result is not None:
            messagebox.showinfo("Wynik", f"Wpisałeś: {result}")

    def openMessageBox(self):
        messagebox.showinfo("Okienko informacyjne", "Jesteś super. Nie zmieniaj się.")

if __name__ == '__main__':
    app = DialogExample()
    app.mainloop()
