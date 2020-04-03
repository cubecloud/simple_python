import divisormaster as dm
from divisormaster import div_guru, div_guru_canon, all_dividers, check_number_simplicity, ask_for_number, max_divider

num = ask_for_number()
print('Проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);')

if check_number_simplicity(num):
    print ('Вы ввели', num , ' - это простое число')
else:
    print ('Вы ввели', num , ' - это составное число')

print('Список всех делителей числа', num)
print (all_dividers(num))

print('Самый большой простой делитель числа', num)
print (max_divider(div_guru(num)))
print ('Каноническое разложение числа', num)
print(div_guru(num))
print(div_guru_canon(num))
print('Самый большой делитель (не обязательно простой) числа',num)
print (max_divider(all_dividers(num)[:-1]))


