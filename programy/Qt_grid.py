import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

class GridExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.label = QLabel("Numer przycisku: -")
        self.grid.addWidget(self.label, 0, 0, 1, 3)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                w=j*3+1+i
                button = QPushButton(f'Przycisk {w}')
                button.clicked.connect(self.buttonClicked)
                self.grid.addWidget(button, i + 1, j, 1, 1)
                self.buttons.append(button)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Qt Siatka')

    def buttonClicked(self):
        button = self.sender()
        button.setText("Kliknięte!")
        index = self.buttons.index(button)
        self.label.setText(f"Numer przycisku: {index}")
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    ex.show()
    sys.exit(app.exec())
