import os
import sqlite3

DB_NAME = 'library.db'

class Book:
    def __init__(self, number, info):
        self.number = number
        self.author = info["автор"]
        self.title = info["назва"]
        self.publisher = info["видавництво"]
        self.genre = info["жанр"]
        self.year = info["рік"]

    def get_data(self):
        return (self.number, self.author, self.title,
                self.publisher, self.genre, self.year)

    def __str__(self):
        return (f"№{self.number}: {self.author}, «{self.title}», "
                f"{self.publisher}, {self.genre}, {self.year}")

class Library:
    COLUMNS = {"number": "number", "author": "author", "title": "title",
               "publisher": "publisher", "genre": "genre", "year": "year"}

    def __init__(self, db_name=DB_NAME):
        self.books = []
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS books
                            (number INTEGER PRIMARY KEY,
                             author TEXT, title TEXT, publisher TEXT,
                             genre TEXT, year INTEGER)""")

    def save_to_db(self, book):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("INSERT OR REPLACE INTO books VALUES (?,?,?,?,?,?)",
                         book.get_data())

    def delete_from_db(self, number):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.execute("DELETE FROM books WHERE number = ?",
                               (number,))
            return cur.rowcount > 0

    def search_in_db(self, **criteria):
        for key in criteria:
            if key not in self.COLUMNS:
                raise ValueError(f"Невідомий критерій пошуку: {key}")
        sql = "SELECT * FROM books"
        if criteria:
            sql += " WHERE " + " AND ".join(
                f"{self.COLUMNS[k]} = ?" for k in criteria)
        with sqlite3.connect(self.db_name) as conn:
            rows = conn.execute(sql, tuple(criteria.values())).fetchall()
        return [Book(r[0], {"автор": r[1], "назва": r[2],
                            "видавництво": r[3], "жанр": r[4], "рік": r[5]})
                for r in rows]

    def load_from_db(self):
        self.books = self.search_in_db()

    def add_book(self, number, info):
        self.books = [b for b in self.books if b.number != number]
        book = Book(number, info)
        self.books.append(book)
        self.save_to_db(book)

    def remove_book(self, number):
        in_db = self.delete_from_db(number)
        for book in self.books:
            if book.number == number:
                self.books.remove(book)
                return True
        return in_db

    def get_book(self, number):
        for book in self.books:
            if book.number == number:
                return book
        return None

    def search(self, author=None, year=None, genre=None, title=None,
               publisher=None):
        result = []
        for book in self.books:
            if author is not None and book.author != author:
                continue
            if year is not None and book.year != year:
                continue
            if genre is not None and book.genre != genre:
                continue
            if title is not None and book.title != title:
                continue
            if publisher is not None and book.publisher != publisher:
                continue
            result.append(book)
        return result

    def show(self):
        if not self.books:
            print("Бібліотека порожня")
        for book in self.books:
            print(book)

def show_list(books):
    if not books:
        print("Нічого не знайдено")
    for book in books:
        print(book)
        
if __name__ == '__main__':
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    lib = Library()
    lib.add_book(1, {"автор": "Тарас Шевченко", "назва": "Кобзар",
                     "видавництво": "Дніпро", "жанр": "поезія", "рік": 1840})
    lib.add_book(2, {"автор": "Іван Франко", "назва": "Захар Беркут",
                     "видавництво": "Основи", "жанр": "роман", "рік": 1883})
    lib.add_book(3, {"автор": "Леся Українка", "назва": "Лісова пісня",
                     "видавництво": "Дніпро", "жанр": "драма", "рік": 1911})
    lib.add_book(4, {"автор": "Іван Франко", "назва": "Мойсей",
                     "видавництво": "Основи", "жанр": "поезія", "рік": 1905})

    print("Усі книги (у пам'яті):")
    lib.show()

    print("\nПошук у базі за автором (Іван Франко):")
    show_list(lib.search_in_db(author="Іван Франко"))

    print("\nПошук у базі за жанром (поезія):")
    show_list(lib.search_in_db(genre="поезія"))

    print("\nПошук у базі за роком (1911):")
    show_list(lib.search_in_db(year=1911))

    print("\nПошук у базі за автором і жанром (Іван Франко, поезія):")
    show_list(lib.search_in_db(author="Іван Франко", genre="поезія"))

    print("\nВидалення книги №2:", lib.remove_book(2))
    print("Видалення неіснуючої книги №10:", lib.remove_book(10))

    print("\nНова бібліотека, дані завантажено з бази:")
    lib2 = Library()
    lib2.load_from_db()
    lib2.show()
