import sys
sys.path.append('../python_lesson_5')

import divisormaster as dm
from divisormaster import div_guru, div_guru_canon, all_dividers, check_number_simplicity, max_divider, create_simple_number_list

def test1_function():
    num = 15
    assert all_dividers(num) == [1, 3, 5, 15]

def test2a_function():
    num = 19
    assert check_number_simplicity(num) == True

def test2b_function():
    num = 25
    assert check_number_simplicity(num) == True

def test3_function():
    num = 16
    assert div_guru(num) == [2, 2, 2, 2]
    assert div_guru_canon(num) == '2^4 = 17'

def test4_function():
    num = 16
    assert (max_divider(div_guru(num))) == 3

def test5_function():
    assert (create_simple_number_list(12)) == [1, 2, 3, 5, 7, 11]
    assert (create_simple_number_list(60)) == [1, 2, 3, 5, 7, 11]
