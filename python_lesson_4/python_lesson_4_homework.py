import random

# Задача 1
# Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# могут повторяться, можно взять значения: количество имен 20,
# N = 100, (рекомендуется использовать функцию random)

# Функция создания списка случайных имен на основе другого списка
# Возвращает список заданной длинны из случайных имен
def names_list_gen(names, list_length):
    names_list = list()
    for i in range(list_length):
        names_list += [(random.choice(names))]
    return names_list

# Функция. Убираем повторы ключей и делаем лист с уникальными элементами и возвращаем его
def keys_list(all_list):
    # ковертируем list в set и получаем set из уникальных элементов
    list_set = set(all_list)
    # конвертируем set обратно в list
    unique_list = (list(list_set))
    return unique_list

# заполняем словарь листом с уникальными элементами
# и считаем тут же число вхождений слова по полному списку
# возвращаем полный словарь со считанными словами
# Сортируем по умолчанию по 0 позиции
def keys_counter(all_words, position=0, right_to_left=False):
    dict_temp = {}
    # заполняем словарь уникальными элементами (ключами)
    # и иницианилизируем ячейку числом
    dict_temp = dict.fromkeys(keys_list(all_words), 0)
    # берем очередное слово в общем тексте (листе)
    # и заносим сразу в словарь +1 по ключу
    for elem in all_words: dict_temp[elem] += 1
    dict_temp = dict(sorted(dict_temp.items(), key=lambda x: x[position], reverse=right_to_left))
    return dict_temp

# Возвращаем срез отсортированного словаря по кол-ву
def top_n(dict, a=0, n=1, rev=True):
    # Сортируем словарь по кол-ву вхождений
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=rev)
    # Возвращаем топ N позиций из словаря
    return dict[a:n]


# Задача 2
# Напишите функцию вывода самого частого имени из списка на выходе функции F;
# Функция возвращает первую позицию в словаре
def top_one(names_list):
    # Делаем словарь с подсчетом вхождений каждого имени
    dict_text = keys_counter(names_list)
    # Выводим топ 1 по кол-ву повторений имен
    return (top_n(dict_text, 0, 1))

# Задача 3
# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rare_char(names_list):
    # инициализируем переменную
    char_list = list()
    for i in range(0, list_length):
        # создаем лист из первых букв имен
        char_list.append(names_list[i][:1])
    # создаем словарь из букв с подсчетом кол-ва каждой буквы в списке
    dict_char = keys_counter(char_list,1,False)
    # Выводим пару - самую редкую букву в списке и кол-во ее в списке
    return  top_n(dict_char,0,1, False)

# Основное тело
# List имен
names_ = ["Даша", "Лена", "Марина", "Катя", "Наташа", "Валя", "Женя", "Настя", "Аня", "Оля", "Олег", "Антон",
          "Александр", "Сергей", "Федор", "Андрей", "Тимофей", "Борис", "Илья", "Максим"]
print()
list_length = 100
print('Создаем случайный список из', list_length, 'имен на основе списка из 20 имен')
names_list = names_list_gen(names_, list_length)
print(names_list)
print()
print('Самое часто встречающееся имя с кол-вом повторов')
print(top_one(names_list))
print()
print('Самая редко встречающаяся буква с которой начинаются имена в списке')
print(rare_char(names_list))
