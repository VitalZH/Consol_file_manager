from HT_package.def_for_test_class import salary, hello_who

assert hello_who('Max') == 'Hello, Max', 'Hello who error'
assert hello_who('Leo') == 'Hello, Leo', 'Hello who error'

assert salary(2, 1) == 4, salary(2, 1)
assert salary(2, 2) == 8

from HT_package.def_for_test_class import function_for_test

list_in = [1, 2, 3, 'abc']
assert function_for_test(list_in) == ' error'