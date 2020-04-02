# задача
#  В файле с логами найти дату самого позднего лога (по метке времени):
log_file_name = 'log'
# Вариант 1
# # открываем и читаем файл
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    max_date_str = ''
    for line in text_file:
        # Читаем строку и сравниваем
        if line[:22] > max_date_str[:22]:
            max_date_str = line
# Выводим дату и время последнего лога
print ("Вариант 1")
print (max_date_str)

# Вариант 2
# открываем и читаем файл
log_file_name = 'log'
#  импортируем re
import re
# Создаем словарь с ключами к листам
dict_data={'Date_and_Time' : [], 'Application' : [], 'Type' : [], 'Message' : []}
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        # Делаем сплит строк регулярным выражением
        log_split = re.split(r'(\d+-\d+-\d+.\d+:\d+:\d+,\d+).-.(\w+).-.(\w+).-.(.*)', line)
        i=1
        # Заполняем словарь по ключам данными
        for key in dict_data.keys():
            dict_data[key].append(log_split[i])
            i +=1
    # Получаем лист с датами по ключу
    date_time_line = (dict_data['Date_and_Time'])
    # Сортируем лист
    date_time_line.sort(reverse=True)
    # Выводим дату и время последнего лога
    print("Вариант 2")
    print(date_time_line[0])
    print()

# Вариант 3
import pandas as pd
log_file = pd.read_csv(log_file_name, sep=' - ', names=['Date_and_Time', 'Application', 'Type', 'Message'], engine = 'python')

print ("Вариант 3")
print(log_file.sort_values('Date_and_Time',  ascending=False).head(1))
print()

# Вариант 4
import datetime
log_dates = []
file = open(log_file_name, 'rb').readlines()
for line in file:
    log_dates.append(datetime.datetime.strptime(line.decode().split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f'))
print ("Вариант 4")
print (max([c for c in log_dates]))
