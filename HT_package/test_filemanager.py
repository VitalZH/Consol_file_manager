from HT_package.def_for_test_class import salary, hello_who

def test_hello_who():
    assert hello_who('Maxx') == 'Hello, Max'

def test2_hello_who():
    assert hello_who('Leo') == 'Hello, Leoxxx', 'Ошибка'

def test_salary():
    assert salary(2, 1) == 3, salary(2, 1)

def test2_salary():
    assert salary(2, 2) == 8

from HT_package.def_for_test_class import function_for_test

list_in = [1, 2, 3, 'abc']
def test_def_for_test_class():
    assert function_for_test(list_in) == [1, 2, 3, 's']

from HT_package.HT_9_victory import get_random_person

def test_get_random_person():
    assert get_random_person() == ('Александр Сергеевич Пушнин', '26.06.1799')