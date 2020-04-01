from datetime import datetime
import re

# открываем и читаем файл
log_file_name = 'log'
with open(log_file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        stroka = re.findall(r'(\d+-\d+.\d+.\d+:\d+:\d+,\d+.-.)', line)
        print(stroka)