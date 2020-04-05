import json
import datetime
import pandas as pd
import csv
import re
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

datafile_name = "cars.csv"
# собираем Ключи из из присланной строки и возвращаем лист с ними
def get_keys_list (line_str):
    # # Делаем сплит строки регулярным выражением
    keys_data=list()
    line_split = re.split(r'\;\s',line_str.strip('\n'))
    for couple in line_split:
        couple_split = re.split(r'\:\s', couple)
        keys_data += couple_split[:1]
    return keys_data

def get_dict_data key
with open(datafile_name, 'r', encoding='utf-8') as text_file:
    keys_list=get_keys_list(text_file.readline())
    print(keys_data)




# with open(datafile_name, 'r', encoding='utf-8') as text_file:
#     # reader = csv.DictReader(text_file, delimiter = ':', fieldnames=keys_list)
#     # reader = csv.Sniffer(text_file, delimiter = ':', fieldnames=keys_list)
#     for row in reader:
#          print(dict(row))

# # csv_data = pd.read_csv(datafile_name, header= None, index_col=[0], sep=',', engine='python', encoding='utf8')
# #csv_data = pd.read_csv(datafile_name, names=['a','b','c','d'], sep=',', engine='python', encoding='utf8')
# csv_data = pd.read_csv(datafile_name, header=None, names=keys_list, engine='python', encoding='utf8')
# print (csv_data.shape)
# print (csv_data)

#
# s= csv_data[0:1]
# print (s)

# for i in csv_data:
#     csv_data.ix[1]


def get_context(brand, model, fconsumption, price):  # возвращает словарь аргументов
    # def get_context(company, result_sku_list): # возвращает словарь аргументов
    return {
        'Brand': brand,
        'Model': model,
        'Consumption': fconsumption,
        'Price': price
        # 'retailer': company,
        # 'sku_list': result_sku_list,
    }


brand = 'Volvo'
model = 'X60'
fconsumption = 13.5
price = 2500000


def from_template(brand, model, fconsumption, price, template, signature):
    template = DocxTemplate(template)
    context = get_context(brand, model, fconsumption, price)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    pic = InlineImage(template, signature, img_size)

    context['pic'] = pic  # adds the InlineImage object to the context
    template.render(context)
    # template.save(brand + '_' + str(datetime.datetime.now().date()) + '_report.docx')
    template.save(brand + '_' + '_report.docx')


def generate_report(brand, model, fconsumption, price):
    template = 'template_for_python .docx'
    signature = 'acc.png'
    document = from_template(brand, model, fconsumption, price, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


generate_report(brand, model, fconsumption, price)
