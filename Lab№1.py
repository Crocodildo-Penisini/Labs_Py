import math

x = float(input("Введіть значення x: "))

c = math.tan(abs(x)) - math.sqrt(math.log(2) + math.log(x)) / math.cbrt(
    math.tan(x) + math.pow(math.cos(1 / x), 1 / 4)
)

print("Значення виразу c = ", c)
