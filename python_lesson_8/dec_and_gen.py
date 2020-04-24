# функция default_timer из модуля timeit более точная
from timeit import default_timer
import tracemalloc



# Считам время. Декоратор
def wtime(f):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = f(*args, **kwargs)
        stop_time = default_timer()
        global delta_time
        delta_time = stop_time - start_time
        print(format(delta_time) + ' сек')
        return result

    return wrapper

# Считаем память. Декоратор
def wmem(f):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        memory_tuple = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        global delta_mem
        delta_mem = memory_tuple[0]
        print(format(delta_mem) + ' bytes\n')
        return result

    return wrapper
@wmem
@wtime
def nat_gen(num):
    for i in range(num):
        yield (i)

@wmem
@wtime
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
    print(str(delta_mem - delta_mem1) + ' bytes')
else:
    print('Генератор натуральных чисел занимает в памяти больше, '
          'чем функция создания списка натуральных чисел и ее данные (от 1 до 1 млн) на')
    print(str(delta_mem1 - delta_mem) + ' bytes')
