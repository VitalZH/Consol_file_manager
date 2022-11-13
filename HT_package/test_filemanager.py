from HT_package.HT_9_victory import salary, hello_who, get_Pushkin


def test_hello_who():
    assert hello_who('Max') == 'Hello, Max'

def test2_hello_who():
    assert hello_who('Leo') == 'Hello, Leo', 'Ошибка'

def test_salary():
    assert salary(2, 1) == 4, salary(2, 1)

def test2_salary():
    assert salary(2, 2) == 8

def test_get_Pushkin():
    assert get_Pushkin() == {'Александр Сергеевич Пушнин': '26.06.1799'}