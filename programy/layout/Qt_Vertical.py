import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class VerticalLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        self.label = QLabel("Numer przycisku:")
        self.vertical_layout.addWidget(self.label)

        self.buttons = []
        for i in range(9):
            button = QPushButton(f'Przycisk {i + 1}')
            button.clicked.connect(self.buttonClicked)
            self.vertical_layout.addWidget(button)
            self.buttons.append(button)

        self.setWindowTitle('Qt Vertical Layout')
        self.setGeometry(100, 100, 200, 300)

    def buttonClicked(self):
        button = self.sender()
        button.setText("Klik!")
        index = self.buttons.index(button)
        self.label.setText(f"Numer przycisku: {index}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VerticalLayoutExample()
    ex.show()
    sys.exit(app.exec())
