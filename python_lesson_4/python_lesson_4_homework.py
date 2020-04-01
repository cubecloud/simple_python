import random


# Задача 1
# Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# могут повторяться, можно взять значения: количество имен 20,
# N = 100, (рекомендуется использовать функцию random)


def names_list_gen(names, list_length):
    names_list = list()
    for i in range(list_length):
        names_list += [(random.choice(names))]
    return names_list


# Убираем повторы и делаем лист с уникальными элементами и возвращаем его
def keys_list(all_list):
    # ковертируем list в set и получаем set из уникальных элементов
    list_set = set(all_list)
    # конвертируем set обратно в list
    unique_list = (list(list_set))
    return unique_list

# заполняем словарь листом с уникальными элементами
# и считаем тут же число вхождений слова по полному списку
# возвращаем полный словарь со считанными словами
def keys_counter(all_words):
    dict_temp = {}
    # заполняем словарь уникальными элементами (ключами)
    # и иницианилизируем ячейку числом
    dict_temp = dict.fromkeys(keys_list(all_words), 0)
    # берем очередное слово в общем тексте (листе)
    # и заносим сразу в словарь +1 по ключу
    for elem in all_words: dict_temp[elem] += 1
    return dict_temp

def top_n(dict, a, n):
    # Сортируем словарь по кол-ву вхождений
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # Возвращаем топ N позиций из словаря
    return dict[a:n]

# Задача 2
# Напишите функцию вывода самого частого имени из списка на выходе функции F;
def top_one(names_list):
    # Делаем словарь с подсчетом вхождений каждого имени
    dict_text = keys_counter(names_list)
    # Выводим топ 1 по кол-ву повторений имен
    return (top_n(dict_text, 0, 1))

# Задача 3
# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rare_char(names_list):
    char_list = list()
    for i in range(0, list_length):
        char_list.append(names_list[i][:1])
    dict_char = keys_counter(char_list)
    couple = top_n(dict_char, (len(dict_char) - 1), (len(dict_char)))
    return couple

# Основное тело
# List имен
names_ = ["Даша", "Лена", "Марина", "Катя", "Наташа", "Валя", "Женя", "Настя", "Аня", "Оля", "Олег", "Антон",
          "Александр", "Сергей", "Федор", "Андрей", "Тимофей", "Борис", "Илья", "Анатолий", "Максим"]

print()
print('Введите длину создаваемого списка имен:')
list_length = 30

while True:
    try:
        list_length = int(input())
        break
    except (TypeError, ValueError):
        print("Неправильный ввод")

print('Создаем случайный список имен на основе списка из 10 имен')
names_list = names_list_gen(names_, list_length)
print(names_list)
print()
print('ТОП 1 имен, наиболее часто встречающихся с кол-вом повторов')
print(top_one(names_list))
print()
print('Самая редко встречающаяся начальная буква имени.')
print(rare_char(names_list))
