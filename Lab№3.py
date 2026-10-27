import random

print("ЗАВДАННЯ 1: Одновимірний масив")

n = int(input("Введіть n: "))

if n <= 0:
    print("Помилка: n повинно бути додатним числом.")
else:
    a = [random.randint(0, 50) for _ in range(3 * n)]
    b = []

    for i in range(0, len(a), 3):
        average = (a[i] + a[i + 1] + a[i + 2]) / 3
        b.append(average)

    print("Початковий масив:", a)
    print("Новий масив:", b)

print("\nЗАВДАННЯ 2: Двовимірний масив")

name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")

n_matrix = sum(1 for char in name if char.isalpha())
m_matrix = sum(1 for char in surname if char.isalpha())

if n_matrix == 0 or m_matrix == 0:
    print("Помилка: ім'я та прізвище повинні містити літери.")
else:
    matrix = [
        [random.randint(-10, 10) for _ in range(n_matrix)]
        for _ in range(m_matrix)
    ]

    print("\nЗгенерована матриця:")
    for row in matrix:
        print(row)

    product = 1
    found = False

    for i in range(m_matrix):
        number = matrix[i][0]

        if number < 0 and number % 2 == 0:
            product *= number
            found = True

    print("\nДобуток від'ємних парних чисел першого стовпчика:")

    if found:
        print(product)
    else:
        print("У першому стовпчику немає від'ємних парних чисел.")
