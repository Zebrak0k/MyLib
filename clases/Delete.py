import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Py_design.delete import Ui_MainWindow

import work_with_db
import make_bookTabele


# Класс удаления книги из базы данных
class Delete(QMainWindow, Ui_MainWindow):
    def __init__(self, table):
        self.table = table
        super().__init__()
        self.setupUi(self)

        self.delete_button.clicked.connect(self.delete)
        self.search_line.textChanged[str].connect(self.search)
        self.exit_button.clicked.connect(self.exit)

        make_bookTabele.make_csv()
        make_bookTabele.make_table(self.bookTable)

    # Функция поиска книги из таблицы
    def search(self):
        if len(self.search_line.text()) < 2 or self.search_line.text() == '':
            make_bookTabele.make_table(self.bookTable)
        else:
            argument = self.search_line.text()
            make_bookTabele.make_table(self.bookTable, argument=argument)

    # Функция удаления книги из таблицы и базы данных
    def delete(self):
        if self.id_book.value() in work_with_db.get_id_books():
            work_with_db.delete(self.id_book.value())
            make_bookTabele.make_table(self.bookTable)
            make_bookTabele.make_table(self.table)

        else:
            self.label_header.setText('Такого id не существует!')

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_lib = Delete()
    my_lib.show()
    sys.exit(app.exec_())
