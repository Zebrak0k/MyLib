import csv

from PyQt5.QtWidgets import QTableWidgetItem

import work_with_db as wwd


# Функция превращат данные из базы в csv файл
def make_csv():
    result = wwd.get_books()
    with open('books.csv', 'w', encoding='utf-8') as file_csv:
        file_csv.write(';'.join(['id', 'Author', 'Book', 'Genre', 'Year', 'Section', 'Read', 'Rating']) + '\n')
        for i in result:
            file_csv.write(';'.join(list(map(lambda x: str(x), i))) + '\n')


# Функция создает таблицу с данными про книги
def make_table(bookTable, argument=False):
    # Создаем актуальный csv файл
    make_csv()

    # Создаем таблицу с данными из csv файла
    with open('books.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        data = sorted(reader, key=lambda x: int(x['id']), reverse=False)

    table_info = dict()

    for i in data:
        table_info[i['Book']] = list(map(lambda x: str(x), [j for j in i.values()]))

    count = 0
    bookTable.setColumnCount(8)

    bookTable.setHorizontalHeaderLabels(
        ['id', 'Author', 'Book', 'Genre', 'Year', 'Section', 'Read', 'Rating'])
    bookTable.setRowCount(0)

    if argument is False:
        for i, row in enumerate(table_info.keys()):
            bookTable.setRowCount(
                bookTable.rowCount() + 1)
            for j, elem in enumerate(table_info[row]):
                bookTable.setItem(
                    i, j, QTableWidgetItem(str(elem)))
    else:
        bookTable.clear()
        table_info = dict()

        for i in data:
            table_info[i['Book']] = list(map(lambda x: str(x), [j for j in i.values()]))

        count = 0
        bookTable.setColumnCount(8)

        bookTable.setHorizontalHeaderLabels(
            ['id', 'Author', 'Book', 'Genre', 'Year', 'Section', 'Read', 'Rating'])
        bookTable.setRowCount(0)

        for i, row in enumerate(table_info.keys()):
            row_2 = row.lower()
            i -= count
            if argument.lower() in row_2:
                bookTable.setRowCount(
                    bookTable.rowCount() + 1)
                for j, elem in enumerate(table_info[row]):
                    bookTable.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            else:
                count += 1
