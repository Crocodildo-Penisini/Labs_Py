# Завдання 1: Розробіть функції для здійснення наступних
# Варіант: 1. Пошук елементів в словнику з значенням ключа.
# Описати функцію обчислення значень функції (визначити m значень заданої функції f(x) на відрізку [a, b]). Результат вивести на екран у вигляді табл. Значення a, b, ε ввести з клавіатури.

import math

def find_by_key(d, key):
    return d.get(key)

def exp2x(x, eps):
    term = 1.0
    y = 1.0
    n = 0
    while True:
        n += 1
        term *= 2 * x / n
        new_y = y + term
        if abs(new_y - y) <= eps:
            return new_y, n
        y = new_y


students = {"Іваненко": 95, "Петренко": 82, "Коваленко": 77}
key = input("Введіть ключ для пошуку: ")
print("Результат:", find_by_key(students, key))

a = float(input("a = "))
b = float(input("b = "))
eps = float(input("eps = "))
m = 10
step = (b - a) / (m - 1)

print("x | f(x) точне | f наближене | точність | ітерацій")
for i in range(m):
    x = a + i * step
    exact = math.exp(2 * x)
    approx, n = exp2x(x, eps)
    print(f"{x:.4f} | {exact:.6f} | {approx:.6f} | {abs(exact - approx):.2e} | {n}")
