import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox("Checkbox"),
            QComboBox(),
            QDateEdit(),
            QDateTimeEdit(),
            QDial(),
            QDoubleSpinBox(),
            QFontComboBox(),
            QLCDNumber(),
            QLabel("Label"),
            QLineEdit(),
            QProgressBar(),
            QPushButton("Button"),
            QRadioButton("Radio Button"),
            QSlider(),
            QSpinBox(),
            QTimeEdit(),
        ]

        for w in widgets:
            w.installEventFilter(self)
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print(f"Kliknięto w widget: {obj.objectName() if obj.objectName() else obj.__class__.__name__}")
        elif event.type() == QEvent.Type.KeyPress:
            if isinstance(obj, QComboBox):
                print(f"Wartość ComboBox: {obj.currentText()}")
            elif isinstance(obj, QDial):
                print(f"Wartość Dial: {obj.value()}")
            elif isinstance(obj, QSlider):
                print(f"Wartość Slider: {obj.value()}")
            elif isinstance(obj, QSpinBox):
                print(f"Wartość SpinBox: {obj.value()}")
            elif isinstance(obj, QCheckBox):
                print(f"Stan Checkbox: {obj.isChecked()}")
            elif isinstance(obj, QLineEdit):
                print(f"Tekst QLineEdit: {obj.text()}")
        return super().eventFilter(obj, event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())