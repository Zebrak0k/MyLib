import shutil

from Py_design.load import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog


# Класс загрузки книги в папку Books
class LoadBook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.load_Button.clicked.connect(self.add)
        self.exit_button.clicked.connect(self.exit)

    # Функция добавления книги в виде pdf файла в папку Books
    def add(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', '', 'pdf File (*.pdf)')
        if res[0] != '':
            shutil.move(res[0], f"Books\{res[0].split('/')[-1]}")
            self.label.setText('Complete')

    def exit(self):
        self.close()
