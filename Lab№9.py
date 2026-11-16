import glob
import os

DATA_DIR = 'data'
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.txt')
LINE12 = '-' * 12

def write_students(filename, students) :
    with open(filename, 'w', encoding = 'utf-8') as f :
for name, mark in students :
f.write(f'{name};{mark}\n')

def append_student(filename, name, mark) :
    with open(filename, 'a', encoding = 'utf-8') as f :
f.write(f'{name};{mark}\n')

def read_students(filename) :
    students = []
    with open(filename, 'r', encoding = 'utf-8') as f :
for line in f :
line = line.strip()
if not line :
    continue
    name, mark = line.split(';')
    students.append((name, float(mark)))
    return students

    def print_file(filename) :
    print(f'\nФайл {filename}:')
    with open(filename, 'r', encoding = 'utf-8') as f :
for line in f :
print(line, end = '')

def find_files(directory, mask = '*.txt') :
    return glob.glob(os.path.join(directory, mask))

    def search_in_file(filename, text) :
    found = []
    with open(filename, 'r', encoding = 'utf-8') as f :
for number, line in enumerate(f, start = 1) :
    if text.lower() in line.lower() :
        found.append((number, line.strip()))
        return found

        def sort_file_by_mark(filename, result_filename, reverse = True) :
        """Сортує дані у файлі за середнім балом і записує в result_filename."""
        students = read_students(filename)
        students.sort(key = lambda s : s[1], reverse = reverse)
        write_students(result_filename, students)

        def task1() :
        os.makedirs(DATA_DIR, exist_ok = True)
        write_students(STUDENTS_FILE, [
            ('Ivanov Ivan', 4.5),
            ('Petrenko Olena', 4.9),
            ('Shevchenko Taras', 3.8),
        ])
        append_student(STUDENTS_FILE, 'Kovalenko Maria', 4.2)
        print_file(STUDENTS_FILE)

        print('\nTXT-файли у каталозі data:', find_files(DATA_DIR))

        word = 'Petrenko'
        print(f'Пошук "{word}":', search_in_file(STUDENTS_FILE, word))

        sorted_file = os.path.join(DATA_DIR, 'students_sorted.txt')
        sort_file_by_mark(STUDENTS_FILE, sorted_file)
        print_file(sorted_file)

        def insert_after_fifth(src, dst) :
        with open(src, 'r', encoding = 'utf-8') as f :
lines = [line.rstrip('\n') for line in f]
lines.insert(5, LINE12)
with open(dst, 'w', encoding = 'utf-8') as f :
f.write('\n'.join(lines) + '\n')

def insert_after_last_without_space(src, dst) :
    with open(src, 'r', encoding = 'utf-8') as f :
lines = [line.rstrip('\n') for line in f]
position = len(lines)
for i, line in enumerate(lines) :
    if ' ' not in line :
position = i + 1
lines.insert(position, LINE12)
with open(dst, 'w', encoding = 'utf-8') as f :
f.write('\n'.join(lines) + '\n')

def task2() :
    src = os.path.join(DATA_DIR, 'input.txt')
    with open(src, 'w', encoding = 'utf-8') as f :
f.write('перший рядок\n'
    'Слово\n'
    'третій рядок тут\n'
    'Python\n'
    'п\'ятий рядок тут\n'
    'шостий\n'
    'ще один рядок\n'
    'кінець\n'
    'останній з пробілом\n')

    out_a = os.path.join(DATA_DIR, 'output_a.txt')
    out_b = os.path.join(DATA_DIR, 'output_b.txt')
    insert_after_fifth(src, out_a)
    insert_after_last_without_space(src, out_b)
    print_file(src)
    print_file(out_a)
    print_file(out_b)

    if __name__ == '__main__':
task1()
print('\n' + '=' * 40)
task2()
