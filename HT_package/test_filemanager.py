'''
3. В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
4. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
'''



# тестирование чистойфункции из файлового менеджера gjkefdnjvfnbxtcrjt
from HT_package import HT_10_def_schet

list_in = [1, 2, 3, 'abc']
assert HT_10_def_schet.function_for_test(list_in) == 'Hello, Max', ' error'
