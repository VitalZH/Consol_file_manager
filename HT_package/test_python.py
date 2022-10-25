'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
'''

#_________задаем тестируемую функцию map1
import math


def newfunc(a):
    return a * a

x = list(map(newfunc, (1, 2, 3, 4)))
print(x)

#тестируем функцию map
def test_newfunc():
    assert list(map(newfunc, (1, 2, 3, 4))) == x

#___________задаем тестируемую функцию map2
def func(a, b):
    return a + b

a = tuple(map(func, [2, 4, 5], [1,2,3]))
print(a)
print(tuple(a))

#тестируем функцию map2
def test_func():
    assert tuple(map(func, [2, 4, 5], [1,2,3])) == a

#___________задаем тестируемую функцию map3
tup = (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup))
print(newtuple)

def test_newtuple():
    assert tuple(map(lambda x: x+3, tup)) == newtuple

#___________задаем тестируемую функцию 4_filter
def func_filter(x):
    if x>=3:
        return x
y = list(filter(func_filter, (1,2,3,4)))

def test_fuct_filter():
    assert list(filter(func_filter, (1,2,3,4))) == y

#___________задаем тестируемую функцию 5_filter
filter_lambda = list(filter(lambda x: (x>=3), (6,2,3,4)))
print(list(filter_lambda))

def test_filter_lambda():
    assert list(filter(lambda x: (x>=3), (6,2,3,4))) == filter_lambda

#___________задаем тестируемую функцию 6_sorted
sorted_numbers = list(sorted([77, 22, 9, -6, 4000]))

def test_sorted_numbers():
    assert list(sorted([77, 22, 9, -6, 4000])) == sorted_numbers

#___________задаем тестируемую функцию 7_pi
'''
написать тесты для функций из библиотеки math: pi, sqrt, pow, hypot. 
'''

import math

def test_pi_num():
    return math.pi * 2
    assert math.pi * 2 == pi_num

def test_sqrt_num():
    return math.sqrt(2)
    assert math.sqrt(2) == sqrt_num

def test_pow_num():
    return math.pow(2, 4)
    assert math.pow(2,4) == pow_num

def test_hypot_num():
    return math.hypot(2, 4)
    assert math.typot(2,4) == hypot_num