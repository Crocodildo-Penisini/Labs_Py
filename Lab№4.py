import string

print("ЗАВДАННЯ 1: Обробка рядків")

sentence = input("Введіть речення: ")

words = sentence.split()
words.sort(key=len)

print("Слова в порядку неспадання довжини:")
print(" ".join(words))

print("\nЗАВДАННЯ 2: Використання множин")

text = input("Введіть текст із цифр і латинських літер: ")

vowels = set("aeiouy")
latin_letters = set(string.ascii_lowercase)

vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char in latin_letters:
        consonant_count += 1

print("Кількість голосних літер:", vowel_count)
print("Кількість приголосних літер:", consonant_count)

if vowel_count > consonant_count:
    print("У тексті більше голосних літер.")
elif consonant_count > vowel_count:
    print("У тексті більше приголосних літер.")
else:
    print("Кількість голосних і приголосних літер однакова.")

print("\nЗАВДАННЯ 3: Використання множин")

text3 = input("Введіть текст із латинських літер: ")

vowels_in_text = set(text3.lower()) & vowels

if text3 and text3.isupper():
    result = sorted(letter.upper() for letter in vowels_in_text)
else:
    result = sorted(vowels_in_text)

if result:
    print("Голосні літери в алфавітному порядку:")
    print(" ".join(result))
else:
    print("У тексті немає голосних літер.")
