# задача
#  В файле с логами найти дату самого позднего лога (по метке времени):
log_file_name = 'log'
# Вариант 1
# # открываем и читаем файл
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    max_date_str = ''
    # Читаем строку и сравниваем
    for line in text_file:
        if line[:23] > max_date_str[:23]:
            max_date_str = line
# Выводим дату и время последнего лога
print("Вариант 1")
print(max_date_str)

# Вариант 2
# открываем и читаем файл
log_file_name = 'log'
#  импортируем модуль re
import re

# Создаем словарь с ключами к листам
dict_data = {'Date_and_Time': [], 'Application': [], 'Type': [], 'Message': []}
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        # Делаем сплит строки регулярным выражением
        log_split = re.split(r'\s[-]\s|\n', line)
        i = 0
        # Заполняем словарь по ключам данными
        for key in dict_data.keys():
            dict_data[key].append(log_split[i])
            i += 1
    # Получаем лист с датами по ключу
    date_time_line = (dict_data['Date_and_Time'])
    # Выводим дату и время последнего лога c помощью функции max
    print("Вариант 2")
    print(max([q for q in date_time_line]))
    print()

# Вариант 3
#  импортируем модуль pandas
import pandas as pd

# заполняем переменную сериями обработанными функциями модуля
log_file = pd.read_csv(log_file_name, sep=' - ', names=['Date_and_Time', 'Application', 'Type', 'Message'],
                       engine='python')
print("Вариант 3")
print(log_file.sort_values('Date_and_Time', ascending=False).head(1))
print()

# Вариант 4
#  импортируем модуль datetime as dt
import datetime as dt

log_dates = []
file = open(log_file_name, 'rb').readlines()
for line in file:
    # заполняем лист датами обработанными функциями модуля
    log_dates.append(dt.datetime.strptime(line.decode().split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f'))
# Выводим дату и время последнего лога c помощью функции max
print("Вариант 4")
print(max([q for q in log_dates]))
