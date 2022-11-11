'''
3. В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
4. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
'''



# тестирование чистойфункции из файлового менеджера gjkefdnjvfnbxtcrjt
'''
from HT_10_def_schet import function_for_test

list_in = [1, 2, 3, 'abc']
assert function_for_test(list_in) == , ' error'
'''

from HT_10_def_schet import salary, hello_who

assert hello_who('Max') == 'Hello, Max', 'Hello who error'
assert hello_who('Leo') == 'Hello, Leo', 'Hello who error'

assert salary(2, 1) == 4, salary(2, 1)
assert salary(2, 2) == 8