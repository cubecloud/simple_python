# Функция удаления пунктуации
# Не вводим возврат корретки в сет пунктуации,
# будет убран позже автоматом
def remove_punctuation (corrected_line):
    empty = str('')
    punct_set = {'.',',','?','!','—','«','»','(',')'}
    for elem in punct_set:
        corrected_line = corrected_line.replace(elem, empty)
    return corrected_line

# Вариант БЕЗ использования collections
# ------------------------------------
# Убираем повторы и делаем лист с уникальными элементами и возвращаем его
def keys_list (all_list):
    # ковертируем list в set и получаем set из уникальных элементов
    list_set = set(all_list)
    # конвертируем set обратно в list
    unique_list = (list(list_set))
    return unique_list

# заполняем словарь листом с уникальными элементами
# и считаем тут же число вхождений слова по полному списку
# возвращаем полный словарь со считанными словами
def keys_counter (all_words):
    dict_temp = {}
    # заполняем словарь уникальными элементами (ключами)
    # и иницианилизируем ячейку числом
    dict_temp = dict.fromkeys(keys_list(all_words),0)
    # берем очередное слово в общем тексте (листе)
    # и заносим сразу в словарь +1 по ключу
    for elem in all_words: dict_temp[elem] += 1
    return dict_temp
# ------------------------------------

# Основное тело программы
# Инициализируем переменную под list
splited_line = list()
# открываем и читаем файл
file_name = 'text_in.txt'
with open(file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        splited_line += remove_punctuation(line).split()
    # переводим в нижний регистр
    lower_line = list(map(lambda x: x.lower(), splited_line))
    # Лемматизация
    # импорт библиотеки
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    lemma = []
    # лематизируем слова и делаем лист
    for word in lower_line:
        normal_word = morph.parse(word)[0]
        lemma.append(normal_word.normal_form)
# Вариант с использованием collections
# ------------------------------------
#     from collections import Counter
#     dict_text = Counter(lemma)
#     print(Counter(lemma).most_common(5))
#     print(dict_text)
# ------------------------------------

# Вариант БЕЗ использования collections
    # Делаем словарь с подсчетом вхождений каждого слова
    dict_text= keys_counter (lemma)
    # Сортируем словарь по кол-ву вхождений
    dict_text = sorted(dict_text.items(), key=lambda x: x[1], reverse=True)
    # Выводим 5 первых по кол-ву вхождений слов
    print ('ТОП 5 разных слов, наиболее часто встречающихся в тексте, с кол-вом повторов')
    print(dict_text [:5])
    print()
    # Выводим весь словарь
    print ('Весь словарь созданный из текста и лемматизированный, с кол-вом повторов каждого слова')
    print(dict_text)
    print()
    # Считаем и выводим кол-во разных слов
    print ('Всего разных слов в словаре')
    print (len(dict_text))
