import json
import datetime
import csv
import re
import timeit
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# Файл с _данными_ состоит из нескольких строк
datafile_name = "cars.txt"
outcsvfile_name = "cars_out.csv"
outjsonfile_name = "cars_out.json"

# Cоздаем словарь из 1(одной) строки передаваемого файла
def get_line_2dict (line_str):
    # # Делаем сплит строки регулярным выражением
    line_dict=dict()
    line_split = re.split(r'\;\s',line_str.strip('\n'))
    for couple in line_split:
        couple_split = re.split(r'\:\s', couple)
        line_dict.update({couple_split[0]:couple_split[1]})
    return line_dict

#Делаем переменные из ключей словаря
def get_dict_data(line_dict):
    for key, value in line_dict.items():
        globals()[key] = value
    return

# Передаем переменные словаря в качестве аргумента.
# Ключи из файла, также являются именами переменных
# и ключами для вставки в template

def generate_report(**line_dict):
    template = 'template_for_python.docx'
    template = DocxTemplate(template)
    img_size = Cm(17)  # sets the size of the image
    pic = InlineImage(template, Image, img_size)
    line_dict['pic'] = pic  # adds the InlineImage object to the context
    template.render(line_dict)
    template.save(Brand + '_' + str(datetime.datetime.now().date()) + '_report.docx')
    return True


# Записываем CSV файл
def save_dict_2csv (text_dict):
    with open(outcsvfile_name, 'w') as csvfile:
        is_this_1st_line = True
        for i in text_dict.keys():
            line_dict= text_dict[i]
            if is_this_1st_line:
                writer = csv.DictWriter(csvfile, fieldnames=line_dict.keys())
                writer.writeheader()
                is_this_1st_line = False
            writer.writerow(line_dict)
    return True


# Записываем JSON файл
def save_dict_2json (text_dict):
    with open(outjsonfile_name, 'w') as jsonfile:
        json.dump(text_dict, jsonfile)
    return True
def test(a):
    a+=1
    return a
# Основное тело
text_dict=dict()
line_dict=dict()

with open(datafile_name, 'r', encoding='utf-8') as textfile:
    i=0
    for line in textfile:
        line_dict=get_line_2dict(line)
        text_dict.update({i:line_dict})
        i+=1
        get_dict_data(line_dict)
        generate_report (**line_dict)
    save_dict_2csv(text_dict) # Записываем CSV
    save_dict_2json(text_dict) # Записываем JSON

    if __name__ == '__main__':
        import timeit
        generate_report (**line_dict)
        print(timeit.timeit("generate_report(**line_dict)", setup="from __main__ import generate_report", number=1, globals=globals()))
        print(timeit.timeit("save_dict_2csv(text_dict)", setup="from __main__ import save_dict_2csv", number=1, globals=globals()))
        print(timeit.timeit("save_dict_2json(text_dict)", setup="from __main__ import save_dict_2json", number=1, globals=globals()))
