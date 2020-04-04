import sys
sys.path.append('../python_lesson_5')
sys.path.append('../python_lesson_4')
import python_lesson_4_homework as ls4
from divisormaster import div_guru, div_guru_canon, all_dividers, check_number_simplicity, max_divider, create_simple_number_list, ask_for_number,_SNUMBERS

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

def test5a_function():
    assert (create_simple_number_list(12)) == [1, 2, 3, 5, 7, 11]
    assert (create_simple_number_list(9)) == [1, 2, 3, 5, 7, 11]
def test5b_function():
    assert (create_simple_number_list(12)) == _SNUMBERS
    assert (_SNUMBERS) == [1, 2, 3, 5, 7, 11]
    assert (create_simple_number_list(9)) == [1, 2, 3, 5, 7, 11]
    assert (create_simple_number_list(9)) == _SNUMBERS
    assert (create_simple_number_list(12)) == [1, 2, 3, 5, 7, 11]

#  Тестируем грязную функцию
def test1_dirty_function():
    names_ = ["Даша", "Лена", "Марина", "Катя", "Наташа", "Валя", "Женя", "Настя", "Аня", "Оля", "Олег", "Антон",
              "Александр", "Сергей", "Федор", "Андрей", "Тимофей", "Борис", "Илья", "Максим"]
    assert (len(ls4.names_list_gen(names_, 5))) == (len(ls4.names_list_gen(names_, 5)))
def test2_dirty_function():
    names_ = ["Даша"]
    assert (ls4.names_list_gen(names_, 4)) == ["Даша", "Даша", "Даша", "Даша", "Даша"]
    assert (len(ls4.names_list_gen(names_, 5))) == (len(ls4.names_list_gen(names_, 5)))
def test3a_dirty_function():
    names_ = ["Даша","Сергей"]
    assert (ls4.names_list_gen(names_, 2)) == ["Даша", "Сергей"]
def test3b_dirty_function():
    names_ = ["Даша","Сергей"]
    assert (ls4.names_list_gen(names_, 2)) == ["Сергей", "Даша"]
def test3c_dirty_function():
    names_ = ["Даша","Сергей"]
    assert (ls4.names_list_gen(names_, 2)) == ["Сергей", "Сергей"]
def test3d_dirty_function():
    names_ = ["Даша","Сергей"]
    assert (ls4.names_list_gen(names_, 2)) == ["Даша", "Даша"]