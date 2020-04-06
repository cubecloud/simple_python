import pytest
import python_lesson_7_homework
from python_lesson_7_homework import generate_report, save_dict_2csv, save_dict_2json, line_dict, text_dict

def test1_function():
    assert generate_report(line_dict) == True

def test2_function():
    # Записываем CSV
    assert save_dict_2csv(text_dict) == True

def test3_function():
    # Записываем JSON
    assert save_dict_2json(text_dict) ==  True

