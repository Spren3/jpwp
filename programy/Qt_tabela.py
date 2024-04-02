import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QTextBrowser, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import QDate, Qt

class MovieInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def sortByColumn(self, index):
        self.movieInfoTable.sortItems(index)

    def initUI(self):
        layout = QVBoxLayout()

        self.dateComboBox = QComboBox()
        self.populateDates()
        self.dateComboBox.currentIndexChanged.connect(self.showMovieInfo)

        self.movieInfoTable = QTableWidget()
        self.movieInfoTable.setColumnCount(5)
        self.movieInfoTable.setHorizontalHeaderLabels(["Tytuł", "Czas trwania", "Godzina emisji", "Kino", "Link do zakupu"])

        layout.addWidget(QLabel("Wybierz datę:"))
        layout.addWidget(self.dateComboBox)
        layout.addWidget(self.movieInfoTable)

        self.setLayout(layout)
        self.resize(800, 600)
        self.movieInfoTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.movieInfoTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.movieInfoTable.horizontalHeader().sectionClicked.connect(self.sortByColumn)

    def populateDates(self):
        today = QDate.currentDate()
        self.dateComboBox.addItem(today.toString(Qt.DateFormat.ISODate))
        for i in range(1, 15):
            date = today.addDays(i)
            self.dateComboBox.addItem(date.toString(Qt.DateFormat.ISODate))

    def showMovieInfo(self, index):
        selectedDate = self.dateComboBox.itemText(index)
        movie_info = [
            ("Ścigany", "120'", "18:00", "Kino A", "http://example.com"),
            ("Adwokat diabla", "90'", "20:00", "Kino B", "http://example.com"),
            ("Skazani na Shawshank", "142'", "21:30", "Kino C", "http://example.com"),
            ("Bękarty wojny", "177'", "20:30", "Kino D", "http://example.com"),
            ("Najmro", "135'", "15:00", "Kino A", "http://example.com"),
        ]

        self.movieInfoTable.setRowCount(len(movie_info))
        for i, (title, duration, time, cinema, link) in enumerate(movie_info):
            self.movieInfoTable.setItem(i, 0, QTableWidgetItem(title))
            self.movieInfoTable.setItem(i, 1, QTableWidgetItem(duration))
            self.movieInfoTable.setItem(i, 2, QTableWidgetItem(time))
            self.movieInfoTable.setItem(i, 3, QTableWidgetItem(cinema))
            self.movieInfoTable.setItem(i, 4, QTableWidgetItem(link))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MovieInfoWidget()
    widget.setWindowTitle("Wykaz Filmów")
    widget.show()
    sys.exit(app.exec())
