import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class ErrorHandlingExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Obsługa błędu w PyQt6")
        self.setGeometry(100, 100, 300, 200)

        button1 = QPushButton("rzuć błąd valueError", self)
        button1.setGeometry(50, 50, 200, 30)
        button1.clicked.connect(self.generateError)

        button2 = QPushButton("Obsługa błędu dzielenia", self)
        button2.setGeometry(50, 100, 200, 30)
        button2.clicked.connect(self.divideByZero)

    def generateError(self):
        try:
            # rzucamy jakis błąd ręcznie
            raise ValueError("Przykładowy błąd")

        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Wystąpił błąd: {str(e)}")

    def divideByZero(self):
        try:
            result = 1 / 0  # Dzielenie przez zero
            QMessageBox.information(self, "Wynik", f"Wynik: {result}")

        except ZeroDivisionError as e:
            QMessageBox.critical(self, "Błąd", f"Podzieliłeś przez zero: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ErrorHandlingExample()
    ex.show()
    sys.exit(app.exec())
