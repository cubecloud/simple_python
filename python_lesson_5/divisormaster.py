# Делаем глобальный список простых чисел

global _SNUMBERS
_SNUMBERS = [1, 2]

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

# Если число не делится нацело - возвращает True
def div_check_int(source_number, i):
    if source_number % i >= 1:
        return True
    else:
        return False

# Если число простое то возвращает True
def check_number_simplicity(number):
    for i in range(2, number):
        # Если число не делится нацело, с этим делителем, то оно _возможно_ простое
        if div_check_int(number, i):
            # не делится - проверим следущий делитель
            continue
        else:
            # Делится нацело - не подходит
            return False
    return True

# создает лист с простыми числами до указанного предела
def create_simple_number_list(quantity):
    if _SNUMBERS != [1, 2] : return _SNUMBERS
    for n in range(3, quantity):
        if check_number_simplicity(n): _SNUMBERS.append(n)
    return _SNUMBERS

# Ввод числа
def ask_for_number():
    print('Введите число =>')
    while True:
        try:
            number = int(input())
            break
        except (TypeError, ValueError):
            print("Неправильный ввод")
    return number

# Каноническое разложение числа и вывод
def div_guru_canon(number):
    canon_dict = keys_counter(div_guru(number))
    res_str = ''
    for i in canon_dict.keys():
        res_str += str(i) + '^' + str(canon_dict[i]) + ' * '
    res_str = res_str[:-3] + ' = ' + str(number)
    return res_str

# По умолчанию делители - список ПРОСТЫХ чисел
# Список dividers может быть любой сортированной последовательностью чисел
def div_guru(number, dividers=_SNUMBERS):
    div_list = list()
    # Отсюда стартует рекурсивная функция
    # -----------------------------------
    def div_number(number):
        # объявляем переменную не локальной, чтобы вернуть данные в функцию выше
        nonlocal div_list
        nonlocal dividers
        # проверка на код завершения и возврат из функции списка делителей в случае _0_
        if number == 0: return div_list
        # берем элемент из списка простых чисел, пропуская 1
        for snumber in dividers[1:]:
            # проверяем, чтобы делитель был больше делимого
            if snumber < number:
                # Если число не делится нацело - возвращает True
                if div_check_int(number, snumber):
                    # не делится проверим следующий делитель
                    continue
                else:  # число делится нацело - можем добавить делитель в список
                    div_list.append(snumber)
                    return div_number(number // snumber)  # и вернуться вызвав рекурсию с результатом
            elif snumber == number:  # Если делимое и делитель одинаковы
                # Добавляем делитель в список и возвращаемся с кодом завершения
                div_list.append(snumber)
                return 0
            else:  # Делитель стал больше делимого - возврат с кодом завершения
                return 0
    # -----------------------------------
    #  Здесь рекурсивная функция заканчивается
    if div_number(number) == 0:
        return div_list

# Создается список со всеми возможными делителями заданного числа
def all_dividers (num):
    all_dividers_numbers = []
    for i in range(1, num+1):
        if num % i == 0: all_dividers_numbers.append(i)
    return all_dividers_numbers

def max_divider (dividers_list):
    return max(dividers_list)

# Main Body
list_length = 1000
print('Инициализация модуля. Создание списка простых чисел до', list_length)
create_simple_number_list(list_length)

if __name__ == '__main__':
    print('Это сам модуль\n')
