import os
import sqlite3

DB_NAME = 'library.db'
FIELDS = ('author', 'title', 'publisher', 'genre', 'year')

class HomeLibrary:
    books = {}

    def __init__(self, number, info):
        self.number = number
        self.author = info.get('author', '')
        self.title = info.get('title', '')
        self.publisher = info.get('publisher', '')
        self.genre = info.get('genre', '')
        self.year = info.get('year', 0)

    def __str__(self):
        return (f'№{self.number}: {self.author} - "{self.title}", '
                f'{self.publisher}, {self.genre}, {self.year}')

    def get_data(self):
        return (self.number, self.author, self.title,
                self.publisher, self.genre, self.year)

    @classmethod
    def add_book(cls, number, info):
        book = cls(number, info)
        cls.books[number] = book
        return book

    @classmethod
    def remove_book(cls, number):
        return cls.books.pop(number, None)

    @classmethod
    def get_book(cls, number):
        return cls.books.get(number)

    @classmethod
    def find(cls, **criteria):
        return [b for b in cls.books.values()
                if all(getattr(b, k) == v for k, v in criteria.items())]

    @staticmethod
    def create_table(db_name=DB_NAME):
        with sqlite3.connect(db_name) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS library
                            (number INTEGER PRIMARY KEY,
                             author TEXT, title TEXT, publisher TEXT,
                             genre TEXT, year INTEGER)""")

    def save_to_db(self, db_name=DB_NAME):
        with sqlite3.connect(db_name) as conn:
            conn.execute("INSERT OR REPLACE INTO library VALUES (?,?,?,?,?,?)",
                         self.get_data())

    @staticmethod
    def delete_from_db(number, db_name=DB_NAME):
        with sqlite3.connect(db_name) as conn:
            cur = conn.execute("DELETE FROM library WHERE number = ?",
                               (number,))
            return cur.rowcount

    @staticmethod
    def find_in_db(db_name=DB_NAME, **criteria):
        allowed = ('number',) + FIELDS
        for key in criteria:
            if key not in allowed:
                raise ValueError(f'Невідоме поле: {key}')
        sql = 'SELECT * FROM library'
        if criteria:
            sql += ' WHERE ' + ' AND '.join(f'{k} = ?' for k in criteria)
        with sqlite3.connect(db_name) as conn:
            rows = conn.execute(sql, tuple(criteria.values())).fetchall()
        return [HomeLibrary(r[0], dict(zip(FIELDS, r[1:]))) for r in rows]

    @classmethod
    def load_from_db(cls, db_name=DB_NAME):
        cls.books.clear()
        for book in cls.find_in_db(db_name):
            cls.books[book.number] = book
        return list(cls.books.values())

def show(title, books):
    print(f'\n{title}')
    if not books:
        print('  (нічого не знайдено)')
    for b in books:
        print(' ', b)

def main():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    HomeLibrary.create_table()

    data = [
        (1, {'author': 'Шевченко Т.', 'title': 'Кобзар',
             'publisher': 'Дніпро', 'genre': 'поезія', 'year': 2010}),
        (2, {'author': 'Франко І.', 'title': 'Захар Беркут',
             'publisher': 'Основи', 'genre': 'роман', 'year': 2005}),
        (3, {'author': 'Шевченко Т.', 'title': 'Гайдамаки',
             'publisher': 'Дніпро', 'genre': 'поезія', 'year': 2012}),
        (4, {'author': 'Леся Українка', 'title': 'Лісова пісня',
             'publisher': 'Знання', 'genre': 'драма', 'year': 2005}),
    ]
    for number, info in data:
        HomeLibrary.add_book(number, info).save_to_db()

    show('Усі книги в базі:', HomeLibrary.find_in_db())
    show('Пошук за автором "Шевченко Т.":',
         HomeLibrary.find_in_db(author='Шевченко Т.'))
    show('Пошук за роком 2005:', HomeLibrary.find_in_db(year=2005))
    show('Пошук за жанром "поезія" і роком 2012:',
         HomeLibrary.find_in_db(genre='поезія', year=2012))

    deleted = HomeLibrary.delete_from_db(2)
    print(f'\nВидалено записів з бази (книга №2): {deleted}')
    HomeLibrary.remove_book(2)

    show('Після видалення (завантажено з бази):', HomeLibrary.load_from_db())
    print('\nКнига за номером 3:', HomeLibrary.get_book(3))

if __name__ == '__main__':
    main()
