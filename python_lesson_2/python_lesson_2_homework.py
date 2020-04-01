#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('Задача 1')
print("Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована")
string_length = 80
qty_of_string = int(3)
zero_string=str('')
for i in range (1,string_length):
    zero_string += '0'
for k in range (qty_of_string):
    print (zero_string)
print()

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Задача 2')
print("Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5")

digit_count=0
for i in range (1,11):
    print('Введите ЦИФРУ №',i)
    while True:
        try:
            digit = int(input())
            if digit >9:
                print("Неправильный ввод")
                continue
            elif digit == 5:
                digit_count += 1
            break
        except (TypeError, ValueError):
            print("Неправильный ввод")
print("Количество введеных пользователем цифр 5 =",digit_count)
print()
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Задача 3')
print("Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран")
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
print()
'''

Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('Задача 4')
print("Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран")
multiply = 1
for i in range(1,11):
    multiply *= i
print(multiply)
print()

'''
Задача 5(А)
Вывести цифры числа на каждой строчке.
'''
print('Задача 5(А)')
print("Вывести цифры числа на каждой строчке")
integer_number = 2129
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print()

'''
Задача 5(Б)
Вывести цифры числа на каждой строчке. В обратном порядке.
'''
print('Задача 5(Б)')
print("Вывести цифры числа на каждой строчке в обратном порядке")
integer_number = 212956
for i in range(0,len(str(integer_number))):
    print(str(integer_number)[i])
print()

'''
Задача 6
Найти сумму цифр числа.
'''
def sum_number (integer_number):
    sum = 0
    while integer_number > 0:
        sum += integer_number%10
        integer_number = integer_number//10
    return sum

mem_number = 55555
print('Задача 6')
print("Найти сумму цифр числа", mem_number, "=", sum_number(mem_number))
print()

'''
Задача 7
Найти произведение цифр числа.
'''
def multiply_number (integer_number):
    multiplication_number = 1
    while integer_number > 0:
        multiplication_number*= integer_number%10
        integer_number = integer_number//10
    return multiplication_number

mem_number = 2222
print('Задача 7')
print("Произведение цифр числа", mem_number, "=", multiply_number(mem_number))
print()
'''

Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
def is_five_present (integer_number):
    while integer_number>0:
        if integer_number%10 == 5:
            return True
            break
        integer_number = integer_number//10
    else: return False

mem_number= 211465
print('Задача 8')
print("Дать ответ на вопрос: есть ли среди цифр числа 5","в числе", mem_number)
if is_five_present(mem_number):
    print("ДА")
else:
    print("НЕТ")
print()
'''
Задача 9
Найти максимальную цифру в числе
'''
def max_digit (integer_number):
    max_number=0
    while integer_number>0:
        if integer_number%10 > max_number:
            max_number = integer_number%10
        integer_number = integer_number//10
    return max_number

mem_number= 2111359
print('Задача 9')
print("Найти максимальную цифру в числе",mem_number)
print("ЭТО ЦИФРА",max_digit(mem_number))
print()
'''

Задача 10
Найти количество цифр 5 в числе
'''
def how_many_five_digits (integer_number):
    count_five=0
    while integer_number>0:
        if integer_number%10 == 5 :
            count_five += 1
        integer_number = integer_number//10
    return count_five

mem_number = 5222225
print('Задача 10')
print("Какое количество цифр 5 в числе",mem_number)
print(how_many_five_digits(mem_number))
