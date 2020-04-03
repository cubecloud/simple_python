import divisormaster as dm
from divisormaster import div_guru, div_guru_canon, all_dividers, check_number_simplicity, ask_for_number

num = ask_for_number()
print('Проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);')

if check_number_simplicity(num):
    print ('Вы ввели', num , ' - это простое число\n')
else:
    print ('Вы ввели', num , ' - это составное число\n')

print('Список всех делителей числа', num)
print (all_dividers(num),'\n')

print('Самый большой простой делитель числа', num)
div_temp = div_guru(num)
print(div_temp[len(div_temp) - 1],'\n')
print ('Каноническое разложение числа', num)
print(div_temp)
print(div_guru_canon(num))

