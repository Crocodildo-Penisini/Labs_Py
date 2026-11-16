class Student:
    def __init__(self, name):
        self.name = name
        self.e1 = 0
        self.e2 = 0
        self.e3 = 0

    def set_marks(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def get_average_mark(self):
        print(self.name, ' - ', (self.e1 + self.e2 + self.e3) / 3)


class Book:
    def __init__(self, number, info):
        self.number = number
        self.author = info["автор"]
        self.title = info["назва"]
        self.publisher = info["видавництво"]
        self.genre = info["жанр"]
        self.year = info["рік"]

    def __str__(self):
        return (f"№{self.number}: {self.author}, «{self.title}», "
                f"{self.publisher}, {self.genre}, {self.year}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, number, info):
        self.books.append(Book(number, info))

    def remove_book(self, number):
        for book in self.books:
            if book.number == number:
                self.books.remove(book)
                return True
        return False

    def get_book(self, number):
        for book in self.books:
            if book.number == number:
                return book
        return None

    def search(self, author=None, year=None, genre=None, title=None, publisher=None):
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


print("=== Модифікований приклад 1 ===")
count = int(input("Кількість студентів: "))
students = []
for i in range(count):
    name = input("Ім'я студента: ")
    s = Student(name)
    e1 = float(input("Оцінка 1: "))
    e2 = float(input("Оцінка 2: "))
    e3 = float(input("Оцінка 3: "))
    s.set_marks(e1, e2, e3)
    students.append(s)

for s in students:
    s.get_average_mark()

print("\n=== Завдання 1. Домашня бібліотека ===")
lib = Library()
lib.add_book(1, {"автор": "Тарас Шевченко", "назва": "Кобзар",
                 "видавництво": "Дніпро", "жанр": "поезія", "рік": 1840})
lib.add_book(2, {"автор": "Іван Франко", "назва": "Захар Беркут",
                 "видавництво": "Основи", "жанр": "роман", "рік": 1883})
lib.add_book(3, {"автор": "Леся Українка", "назва": "Лісова пісня",
                 "видавництво": "Дніпро", "жанр": "драма", "рік": 1911})
lib.add_book(4, {"автор": "Іван Франко", "назва": "Мойсей",
                 "видавництво": "Основи", "жанр": "поезія", "рік": 1905})

print("\nУсі книги:")
lib.show()

print("\nДоступ до книги за номером 3:")
print(lib.get_book(3))

print("\nПошук за автором (Іван Франко):")
show_list(lib.search(author="Іван Франко"))

print("\nПошук за жанром (поезія):")
show_list(lib.search(genre="поезія"))

print("\nПошук за роком (1911):")
show_list(lib.search(year=1911))

print("\nПошук за автором і жанром (Іван Франко, поезія):")
show_list(lib.search(author="Іван Франко", genre="поезія"))

print("\nВидалення книги №2:", lib.remove_book(2))
print("Видалення неіснуючої книги №10:", lib.remove_book(10))

print("\nБібліотека після видалення:")
lib.show()
