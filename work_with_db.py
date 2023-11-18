import sqlite3

path = f'/TestMyLib/MyLib_db'


# Функция возаращает список книг с данными про эти книги
def get_books():
    result = []
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    arr = cursor.execute("""
            SELECT * FROM {}
            """.format("Books")).fetchall()
    for i in arr:
        i = list(i)
        i[1] = id_to_author(i[1])
        i[3] = id_to_genre(i[3])
        i[5] = id_to_section(i[5])
        result.append(i)

    connect.commit()
    connect.close()
    return result


# Функция возаращает id книг из базы данных
def get_id_books():
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    result = cursor.execute("""
                SELECT id FROM {}
                """.format("Books")).fetchall()
    connect.commit()
    connect.close()
    result = list(map(lambda x: x[0], result))
    return result


# Функция возаращает автора и книгу из базы данных
def get_author_and_book():
    result = []
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    arr = cursor.execute("""
                SELECT * FROM {}
                """.format("Books")).fetchall()
    for i in arr:
        i = list(i)
        i[1] = id_to_author(i[1])
        i[3] = id_to_genre(i[3])
        i[5] = id_to_section(i[5])
        result.append(i[1:3])

    connect.commit()
    connect.close()
    return result


# Функция возаращает длину таблицы книг из базы данных
def length_db(word):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    result = cursor.execute("""
        SELECT * FROM {}
        """.format(word)).fetchall()
    connect.commit()
    connect.close()
    return len(result)


# Функция добавляет автора книги в базу данных
def add_author_in_db(author):
    add = tuple([length_db('Authors') + 1, author])
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(
        """INSERT INTO Authors
        (id, Author) 
        VALUES
        {}""".format(add))
    connect.commit()
    connect.close()


# Функция превращае автора книги в его id
def author_to_id(author):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    list_authors = list(cursor.execute("""SELECT Author FROM Authors""").fetchall())
    author = (author,)
    if list_authors != [] and author in list_authors:
        result = cursor.execute("""SELECT id FROM Authors WHERE Author = '{}'""".format(author[0])).fetchall()[0][0]
    else:
        add_author_in_db(author[0])
        result = cursor.execute("""SELECT id FROM Authors WHERE Author = '{}'""".format(author[0])).fetchall()[0][0]
    connect.commit()
    connect.close()
    return result


# Функция добавляет жанр книги в базу данных
def add_genre_in_db(genre):
    add = tuple([length_db('Genres') + 1, genre])
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(
        """INSERT INTO Genres
        (id, Genre) 
        VALUES
        {}""".format(add))
    connect.commit()
    connect.close()


# Функция превращает жанр книги в его id
def genre_to_id(genre):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    list_genres = list(cursor.execute("""SELECT Genre FROM Genres""").fetchall())
    genre = (genre,)
    if list_genres != [] and genre in list_genres:
        result = cursor.execute("""SELECT id FROM Genres WHERE Genre = '{}'""".format(genre[0])).fetchall()[0][0]
    else:
        add_genre_in_db(genre[0])
        result = cursor.execute("""SELECT id FROM Genres WHERE Genre = '{}'""".format(genre[0])).fetchall()[0][0]
    connect.commit()
    connect.close()
    return result


# Функция добавляет книгу в базу данных
def add_book_in_db(arr):
    add = arr
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    add[0] = author_to_id(add[0])
    add[2] = genre_to_id(add[2])
    add[4] = cursor.execute("""SELECT id FROM Section WHERE name_section = '{}'""".format(add[4])).fetchall()[0][0]
    add = tuple([add[0], add[1], add[2], add[3], add[4], add[5], add[6]])
    cursor.execute(
        """INSERT INTO Books
        (Author_id, Book, Genre, Year, Section_id, Read, Rating) 
        VALUES
        {}""".format(add))
    connect.commit()
    connect.close()


# Функция превращает id книги в её жанр из базы данных
def id_to_genre(id):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    result = cursor.execute("""SELECT Genre FROM Genres WHERE id = {}""".format(id)).fetchall()[0][0]
    connect.commit()
    connect.close()
    return result


# Функция превращает id автора в его имя из базы данных
def id_to_author(id):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    result = cursor.execute("""SELECT Author FROM Authors WHERE id = {}""".format(id)).fetchall()[0][0]
    connect.commit()
    connect.close()
    return result


# Функция превращает id секции книг в название этой секции из базы данных
def id_to_section(id):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    result = cursor.execute("""SELECT name_section FROM Section WHERE id = {}""".format(id)).fetchall()[0][0]
    connect.commit()
    connect.close()
    return result


# Функция удаляет книгу из базы данных
def delete(id):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""
        DELETE FROM Books WHERE id = {}
        """.format(id))
    connect.commit()
    connect.close()
