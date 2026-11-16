def print_models(unprinted_designs, completed_models) :
    while unprinted_designs :
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

        def show_completed_models(completed_models) :
        print("\nThe following models have been printed:")
        for model in completed_models :
print(model)

def sort_list(lst) :
    return sorted(lst)

    def find_value(lst, value) :
    return[i for i in range(len(lst)) if lst[i] == value]

    def find_sequence(lst, seq) :
    k = len(seq)
    return[i for i in range(len(lst) - k + 1) if lst[i:i + k] == seq]

    def five_min(lst) :
    return sorted(lst)[:5]

    def five_max(lst) :
    return sorted(lst, reverse = True)[:5]

    def average(lst) :
    return sum(lst) / len(lst)

    def unique(lst) :
    result = []
    for x in lst :
if x not in result :
result.append(x)
return result

print("=== Завдання 1 ===")
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\n=== Завдання 2 ===")
try :
    data = [int(x) for x in input("Введіть список чисел через пробіл: ").split()]
    value = int(input("Значення для пошуку: "))
    seq = [int(x) for x in input("Послідовність для пошуку через пробіл: ").split()]

    print("Сортування:", sort_list(data))
    print("Індекси значення:", find_value(data, value))
    print("Індекси послідовності:", find_sequence(data, seq))
    print("П'ять мінімальних:", five_min(data))
    print("П'ять максимальних:", five_max(data))
    print("Середнє арифметичне:", average(data))
    print("Без повторів:", unique(data))
    except ValueError :
print("Помилка: потрібно вводити цілі числа")
except ZeroDivisionError :
print("Помилка: список порожній")
