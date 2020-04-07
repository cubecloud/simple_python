# функция default_timer из модуля timeit более точная
from timeit import default_timer
import os
import psutil


# Считам время. Декоратор
def wtime(f):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = f(*args, **kwargs)
        stop_time = default_timer()
        global delta_time
        delta_time = stop_time - start_time
        print(format(delta_time) + ' сек\n')
        return result

    return wrapper


# Считаем память. Декоратор
def wmem(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start_mem = proc.memory_info().rss
        result = f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        stop_mem = proc.memory_info().rss
        global delta_mem
        delta_mem = ((stop_mem - start_mem) / 1024)
        print(format(delta_mem) + ' kbytes')
        return result

    return wrapper


@wtime
@wmem
def nat_gen(num):
    for i in range(num):
        yield (i)


@wtime
@wmem
def nat_list(num):
    n_list = list()
    for i in range(num):
        n_list.append(i)
    return n_list


print('Генератор натуральных чисел от 1 до 1 000 000')
print('Время работы и занимаемая память')
nat_gen(1000000)
delta_time1 = delta_time
delta_mem1 = delta_mem

print('Создание списка натуральных чисел от 1 до 1 000 000')
print('Время работы и занимаемая память')
nat_list(1000000)
if delta_time1 < delta_time:
    print('Генератор натуральных чисел быстрее, чем создание списка натуральных чисел (от 1 до 1 млн) на')
    print(str(delta_time - delta_time1) + ' сек')
else:
    print('Генератор натуральных чисел медленее, чем создание списка натуральных чисел (от 1 до 1 млн) на')
    print(str(delta_time1 - delta_time) + ' сек')
if delta_mem1 < delta_mem:
    print('Генератор натуральных чисел занимает в памяти меньше, '
          'чем функция создания списка натуральных чисел и ее данные (от 1 до 1 млн) на')
    print(str(delta_mem - delta_mem1) + ' Kbytes')
else:
    print('Генератор натуральных чисел занимает в памяти больше, '
          'чем функция создания списка натуральных чисел и ее данные (от 1 до 1 млн) на')
    print(str(delta_mem1 - delta_mem) + ' Kbytes')
