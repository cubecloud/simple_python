from divisormaster import div_guru, div_guru_canon, all_dividers, check_number_simplicity, ask_for_number, max_divider


def test1_function():
    num = 15
    assert all_dividers(num) == [1, 3, 5, 15]

def test2_function():
    num = 19
    assert check_number_simplicity(num) == True

def test3_function():
    num = 19
    assert check_number_simplicity(num) == True

def test4_function():
    num = 16
    assert div_guru(num) == [2, 2, 2, 2]
    assert div_guru_canon(num) == '2^4 = 17'

def test5_function():
    num = 16
    assert (max_divider(div_guru(num))) == 3



