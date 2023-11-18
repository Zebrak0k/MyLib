from PyQt5.QtWidgets import QMainWindow
from Py_design.MyLib import Ui_MainWindow

from clases.AddBook import AddBook
import make_bookTabele
from clases.Delete import Delete
from clases.readBook import Book
from clases.loadBook import LoadBook


# Класс основного окна
class MyLib(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключаем кнопки к их функциям
        self.new_book.clicked.connect(self.add_new_book)
        self.search_line.textChanged[str].connect(self.search)
        self.Delete_book.clicked.connect(self.delete)
        self.Select_book.clicked.connect(self.read)
        self.load_book.clicked.connect(self.loadBook)

        make_bookTabele.make_csv()
        make_bookTabele.make_table(self.bookTable)

        self.bookTable = self.bookTable

    # Функция поиска книги в таблице
    def search(self):
        if len(self.search_line.text()) < 2 or self.search_line.text() == '':
            make_bookTabele.make_table(self.bookTable)
        else:
            argument = self.search_line.text()
            make_bookTabele.make_table(self.bookTable, argument=argument)

    def add_new_book(self):
        self.add_bookWindow = AddBook(self.bookTable)
        self.add_bookWindow.show()

    def read(self):
        self.readBook = Book()
        self.readBook.show()

    def delete(self):
        self.delete_book = Delete(self.bookTable)
        self.delete_book.show()

    def loadBook(self):
        self.load_book = LoadBook()
        self.load_book.show()
