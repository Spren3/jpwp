import tkinter as tk
from tkinter import filedialog, messagebox

class MenuExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.title("Pasek narzędzi i zapis Tkinter")
        self.geometry("400x300")

        self.textEdit = tk.Text(self)
        self.textEdit.pack(fill=tk.BOTH, expand=True)

        main_menu = tk.Menu(self)
        self.config(menu=main_menu)

        file_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="Plik", menu=file_menu)

        file_menu.add_command(label="Nowy", command=self.newFile)
        file_menu.add_command(label="Otwórz", command=self.openFile)
        file_menu.add_command(label="Zapisz", command=self.saveFile)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjdź", command=self.closeEvent)

        edit_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="Edytuj", menu=edit_menu)

        edit_menu.add_command(label="Wytnij", command=self.cutText)
        edit_menu.add_command(label="Kopiuj", command=self.copyText)
        edit_menu.add_command(label="Wklej", command=self.pasteText)

        self.current_file = ""

    def newFile(self):
        if self.textEdit.get("1.0", "end-1c").strip():
            reply = messagebox.askyesnocancel("Niezapisane zmiany", "Czy chcesz zapisać przed utworzeniem nowego pliku?")
            if reply is None:
                return
            elif reply:
                self.saveFile()
        self.textEdit.delete("1.0", tk.END)
        self.current_file = ""

    def openFile(self):
        if self.textEdit.get("1.0", "end-1c").strip():
            reply = messagebox.askyesnocancel("Niezapisane zmiany", "Czy chcesz zapisać przed otworzeniem innego pliku?")
            if reply is None:
                return
            elif reply:
                self.saveFile()

        filename = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if filename:
            with open(filename, "r") as file:
                self.textEdit.delete("1.0", tk.END)
                self.textEdit.insert(tk.END, file.read())
                self.current_file = filename

    def saveFile(self):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
            if not self.current_file:
                return
        with open(self.current_file, "w") as file:
            file.write(self.textEdit.get("1.0", tk.END))

    def closeEvent(self):
        if self.textEdit.get("1.0", "end-1c").strip():
            reply = messagebox.askyesnocancel("Niezapisane zmiany", "Czy chcesz zapisać przed zamknięciem?")
            if reply is None:
                return
            elif reply:
                self.saveFile()
        self.destroy()

    def cutText(self):
        self.textEdit.event_generate("<<Cut>>")

    def copyText(self):
        self.textEdit.event_generate("<<Copy>>")

    def pasteText(self):
        self.textEdit.event_generate("<<Paste>>")

if __name__ == '__main__':
    app = MenuExample()
    app.mainloop()
