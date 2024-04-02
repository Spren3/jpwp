import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QAction

class MenuExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pasek narzędzi i zapis PyQt6")
        self.setGeometry(100, 100, 400, 300)

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("Plik")
        edit_menu = main_menu.addMenu("Edytuj")

        new_action = QAction("Nowy", self)
        new_action.triggered.connect(self.newFile)
        file_menu.addAction(new_action)

        open_action = QAction("Otwórz", self)
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

        save_action = QAction("Zapisz", self)
        save_action.triggered.connect(self.saveFile)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("Wyjdź", self)
        exit_action.triggered.connect(self.closeEvent)
        file_menu.addAction(exit_action)

        cut_action = QAction("Wytnij", self)
        cut_action.triggered.connect(self.cutText)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Kopiuj", self)
        copy_action.triggered.connect(self.copyText)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Wklej", self)
        paste_action.triggered.connect(self.pasteText)
        edit_menu.addAction(paste_action)

        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        self.current_file = ""

    def newFile(self):
        if self.textEdit.toPlainText().strip():
            reply = QMessageBox.question(self, "Niezapisane zmiany", "Czy chcesz zapisać przed utworzeniem nowego pliku?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Cancel:
                return
            elif reply == QMessageBox.StandardButton.Yes:
                self.saveFile()
        self.textEdit.clear()
        self.current_file = ""

    def openFile(self):
        if self.textEdit.toPlainText().strip():
            reply = QMessageBox.question(self, "Niezapisane zmiany", "Czy chcesz zapisać przed otworzeniem innego pliku?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Cancel:
                return
            elif reply == QMessageBox.StandardButton.Yes:
                self.saveFile()

        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if filename:
            with open(filename, "r") as file:
                self.textEdit.setPlainText(file.read())
                self.current_file = filename

    def saveFile(self):
        if not self.current_file:
            self.current_file, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)")
            if not self.current_file:
                return
        with open(self.current_file, "w") as file:
            file.write(self.textEdit.toPlainText())

    def closeEvent(self, event):
        if self.textEdit.toPlainText().strip():
            reply = QMessageBox.question(self, "Niezapisane zmiany", "Czy chcesz zapisać przed wyjściem?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
            elif reply == QMessageBox.StandardButton.Yes:
                self.saveFile()
        event.accept()

    def cutText(self):
        self.textEdit.cut()

    def copyText(self):
        self.textEdit.copy()

    def pasteText(self):
        self.textEdit.paste()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuExample()
    ex.show()
    sys.exit(app.exec())
