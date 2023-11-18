from pathlib import Path

from PyQt5 import QAxContainer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import os


# Класс прочтения книги из папки Books
class Book(QWidget):
    def __init__(self, parent=None):
        super(Book, self).__init__(parent)
        self.setWindowTitle("ReadBook")

        stylesheet = """
            QWidget
            {
            background-color: rgb(26,26,26);
            }
            """
        self.main_layout = QVBoxLayout(self)

        self.setStyleSheet(stylesheet)
        self.WebBrowser = QAxContainer.QAxWidget(self)
        self.WebBrowser.resize(800, 500)
        self.WebBrowser.setStyleSheet(stylesheet)
        self.WebBrowser.setFocusPolicy(Qt.StrongFocus)
        self.WebBrowser.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.main_layout.addWidget(self.WebBrowser)

        self.f = 'Books'
        self.f = Path(os.path.abspath(self.f)).as_uri()
        self.WebBrowser.dynamicCall('Navigate(const QString&)', self.f)
