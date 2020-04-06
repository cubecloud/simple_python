import json
import datetime
import csv
import re
import docx
import timeit
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# Файл с _данными_ состоит из нескольких строк
datafile_name = "cars.txt"

# Cоздаем словарь из 1(одной) строки передаваемого файла
def get_line_2dict (line_str):
    # # Делаем сплит строки регулярным выражением
    line_dict=dict()
    line_split = re.split(r'\;\s', line_str.strip('\n'))
    for couple in line_split:
        couple_split = re.split(r'\:\s', couple)
        line_dict.update({couple_split[0]: couple_split[1]})
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
    pic = InlineImage (template, Image, img_size)
    line_dict['pic'] = pic  # adds the InlineImage object to the context
    template.render(line_dict)
    global outdocxfile_name
    outdocxfile_name= (Brand + '_' + str(datetime.datetime.now().date()) + '_report.docx')
    template.save(outdocxfile_name)
    return True


# Записываем CSV файл
def save_dict_2csv (line_dict):
    global outcsvfile_name
    outcsvfile_name =(Brand + '_' + str(datetime.datetime.now().date()) + '_report.csv')
    with open(outcsvfile_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=line_dict.keys())
        writer.writeheader()
        writer.writerow(line_dict)
    return True

# Записываем JSON файл
def save_dict_2json (line_dict):
    global outjsonfile_name
    outjsonfile_name =(Brand + '_' + str(datetime.datetime.now().date()) + '_report.json')
    with open(outjsonfile_name, 'w') as jsonfile:
        json.dump(line_dict, jsonfile)
    return True


def add_docx_report_time (time_elapsed):
    doc = docx.Document(outdocxfile_name)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    time_str = ('Отчет сгенерирован за ' + str(time_elapsed) + ' сек')
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph(time_str)
    doc.save(outdocxfile_name)
    return


def add_csv_report_time (time_elapsed):
    # outcsvfile_name =(Brand + '_' + str(datetime.datetime.now().date()) + '_report.csv')
    with open(outcsvfile_name, 'r') as csvfile:
        line_dict=dict()
        reader = csv.DictReader(csvfile)
        for row in reader:
            line_dict=row
            line_dict.update({'GenTime':str(time_elapsed)})
        save_dict_2csv (line_dict)
    return True

def add_json_report_time (time_elapsed):
    # outjsonfile_name =(Brand + '_' + str(datetime.datetime.now().date()) + '_report.json')
    with open(outjsonfile_name, 'r') as jsonfile:
        file_content = jsonfile.read()
        line_dict = json.loads(file_content)
        line_dict.update({'GenTime':str(time_elapsed)})
        save_dict_2json (line_dict)
    return True


# Основное тело
text_dict=dict()

line_dict=dict()

with open(datafile_name, 'r', encoding='utf-8') as textfile:
    for line in textfile:
        line_dict=get_line_2dict(line)
        get_dict_data(line_dict)
        time_elapsed = timeit.timeit("generate_report(**line_dict)", setup="from __main__ import generate_report", number=1, globals=globals())
        add_docx_report_time(time_elapsed)
        time_elapsed = timeit.timeit("save_dict_2csv(line_dict)", setup="from __main__ import save_dict_2csv", number=1, globals=globals())
        add_csv_report_time(time_elapsed)
        time_elapsed = (timeit.timeit("save_dict_2json(line_dict)", setup="from __main__ import save_dict_2json", number=1, globals=globals()))
        add_json_report_time (time_elapsed)