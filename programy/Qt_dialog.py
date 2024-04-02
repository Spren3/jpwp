import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QInputDialog

class DialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Okno dialogowe PyQt6")
        self.setGeometry(100, 100, 300, 200)

        button1 = QPushButton("Otwórz aby wpisać", self)
        button1.setGeometry(50, 50, 200, 30)
        button1.clicked.connect(self.openSimpleDialog)

        button2 = QPushButton("Kliknij aby zobaczyć wiadomość", self)
        button2.setGeometry(50, 100, 200, 30)
        button2.clicked.connect(self.openMessageBox)

    def openSimpleDialog(self):
        result, ok = QInputDialog.getInt(self, "Okienko do wpisania", "Wpisz liczbę:")
        if ok:
            QMessageBox.information(self, "Wynik", f"Wpisałeś: {result}")

    def openMessageBox(self):
        QMessageBox.information(self, "Okienko informacyjne", "Jesteś super. Nie zmieniaj się.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DialogExample()
    ex.show()
    sys.exit(app.exec())
