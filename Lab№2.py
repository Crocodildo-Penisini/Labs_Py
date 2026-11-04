import math

print("Результат обчислення:")

for i in range(2, 9) :
    t = i / 10
    y = (math.tan(2 * t) - 3 * t) / (t + 3)
    k = i - 1

    print(f"t{k} = {t}, y{k} = {y}")
