import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QThread
from animated_toggle import AnimatedToggle

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    mainToggle = AnimatedToggle()
    secondaryToggle = AnimatedToggle(
        checked_color="#FFB000",
        pulse_checked_color="#44FFB000"
    )
    mainToggle.setFixedSize(mainToggle.sizeHint())
    secondaryToggle.setFixedSize(mainToggle.sizeHint())
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Wybierz wszystko"))
    layout.addWidget(mainToggle)
    layout.addWidget(QLabel("Tryb ciemny"))
    layout.addWidget(secondaryToggle)
    window.setLayout(layout)
    mainToggle.stateChanged.connect(secondaryToggle.setChecked)

    def change_background_color():
        if secondaryToggle.isChecked():
            window.setStyleSheet("background-color: black; color: white;")
        else:
            window.setStyleSheet("")

    secondaryToggle.stateChanged.connect(change_background_color)

    window.show()
    sys.exit(app.exec())