from timeit import default_timer
import os
import psutil


def wtime(f):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = f(*args, **kwargs)
        stop_time = default_timer()
        delta_time = stop_time - start_time
        print(format(delta_time) + ' сек\n')
        return result
    return wrapper


def wmem(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start_mem = proc.memory_info().rss
        result = f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        stop_mem = proc.memory_info().rss
        delta_mem = ((stop_mem - start_mem)/1024)
        print(format(delta_mem) + ' kbytes')
        return result
    return wrapper

@wtime
@wmem
def nat_gen(num):
    for i in range(num):
        yield(i)

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
print('Создание списка натуральных чисел от 1 до 1 000 000')
print('Время работы и занимаемая память')
nat_list(1000000)