from PyQt5.QtWidgets import QMainWindow, QButtonGroup
from Py_design.addBook import Ui_MainWindow

import work_with_db
import make_bookTabele
import PyQt5.uic

# Класс добавления книги в базу данных
class AddBook(QMainWindow, Ui_MainWindow):
    def __init__(self, table):
        self.table = table
        super().__init__()
        self.setupUi(self)

        self.add_book_pushButton.clicked.connect(self.complete)
        self.exit_button.clicked.connect(self.exit)

        self.group_1 = QButtonGroup()
        self.group_1.addButton(self.fiction_radioButton)
        self.group_1.addButton(self.technical_radioButton)
        self.group_1.addButton(self.self_help_radioButton)

        self.group_2 = QButtonGroup()
        self.group_2.addButton(self.yes_radioButton)
        self.group_2.addButton(self.no_radioButton)
        self.group_2.addButton(self.during_radioButton)

    # Функция находит активный Radiobutton из соответствующей группы и возвращает текст кнопки
    # или пустую строку если ни одна кнопка не активна
    def search_on(self, arr):
        for i in arr.buttons():
            if i.isChecked():
                return i.text()
        return ''

    # Функция добавления книги в базу данных
    def complete(self):
        add = [self.author_lineEdit.text(), self.book_lineEdit.text(), self.genre_lineEdit.text(),
               self.year_lineEdit.text(),
               self.search_on(self.group_1), self.search_on(self.group_2), self.rating_SpinBox.value()]
        add = list(map(lambda x: x.capitalize() if type(x) is str else x, add))
        if add[0:2] in work_with_db.get_author_and_book():
            self.label_header.setText('Такая книга уже есть!')
        else:
            if '' in add:
                self.label_header.setText('Вы заполнили не все пункты!')
            else:
                work_with_db.add_book_in_db(add)
                self.label_header.setText('Complete!')
                make_bookTabele.make_table(self.table)

        make_bookTabele.make_csv()

    def exit(self):
        self.close()
