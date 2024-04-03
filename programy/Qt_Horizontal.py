import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel

class HorizontalLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.horizontal_layout = QHBoxLayout()
        self.setLayout(self.horizontal_layout)

        self.label = QLabel("Numer przycisku:")
        self.horizontal_layout.addWidget(self.label)

        self.buttons = []
        for i in range(9):
            button = QPushButton(f'Przycisk {i + 1}')
            button.clicked.connect(self.buttonClicked)
            self.horizontal_layout.addWidget(button)
            self.buttons.append(button)

        self.setWindowTitle('Qt Horizontal Layout')
        self.setGeometry(100, 100, 300, 200)

    def buttonClicked(self):
        button = self.sender()
        button.setText("Klik!")
        index = self.buttons.index(button)
        self.label.setText(f"Numer przycisku: {index}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HorizontalLayoutExample()
    ex.show()
    sys.exit(app.exec())
