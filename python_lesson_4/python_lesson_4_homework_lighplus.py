# открываем и читаем файл
file_name = 'text_in.txt'
with open(file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        splited_line += remove_punctuation(line).split()
