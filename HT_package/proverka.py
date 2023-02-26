# пример работы со списками
'''
s = [[1, 2, 3, 4], [4, 5, 6]]
print(f'num#1 {s[0]}')
print(f'num#2 {s[1]}')
m = s[0]
print(f'num#4 {m}')
print(f'num#5 {s[0][2]}')
s[0][1] = 7
print(f'num#7 {s}')
print(f'num#8 {m}')
m[2] = 9
print(f'num#10 {s[0]}')
print(f'num#11 {m}')
s[1].append(12)
print(f'num#13 {s[1]}')
'''
import random
from random import randint

# 1.блок выбора 15 случайных чисел для карточки и разбиваю на три вложенных списка
list_15 = [randint(0, 90) for i in range(15)]  # генератор списка из 15 случайных чисел от 0 до 90
print(list_15)
split_list_15 = [list_15[:5], list_15[5:10], list_15[10:]]
print(split_list_15)

# 2.блок реализации пустой карточки для игры Лото
blank_karta = [['1', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
               ['-', '-', '-', '-', '-', '-', '-', '-', '9']]
for row in blank_karta:
    print('print row', row)
    # генератор позиц (неповтор) в линии карты (range +1 не включая последний элемент)
    ind_in_lin = sorted(random.sample(range(0, 10), 5))
    print('ind_in_lin;', ind_in_lin)
    # заполнение позиц в линии карты значениями из split_list_15
    for ind in ind_in_lin:
        row[ind] = split_list_15[row[] ][ind]
    print('print row', row)
    # Вывод на экран карточки, используя генератора строки из списка через Join
    #print(' '.join(str(elem) for elem in row))
#print(blank_karta)

'''
blank_karta = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
split_list_15 = [[67, 87, 37, 32, 53],
                 [33, 29, 3, 48, 28],
                 [1, 51, 14, 32, 24]]
ind_in_lin = [0, 2, 4, 6, 8]


print('--Вар 1- Мой -')
for i in range(3):
    for j, val in enumerate(ind_in_lin):
        blank_karta[i][val] = split_list_15[i][j]
    print(f'линия{i}: {blank_karta[i]}')
print('-----')

print('--вар 2 - Ира --')
for i in range(len(blank_karta)):
    num_in_split_15 = 0
    for j in range(len(blank_karta[i])):
        if j in ind_in_lin:
            blank_karta[i][j] = split_list_15[i][num_in_split_15]
            num_in_split_15 += 1
    print(blank_karta[i])
'''
