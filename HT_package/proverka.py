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

# 1.блок выбора 15 случайных чисел для карточки
list_15 = [randint(0, 90) for i in range(15)] # генератор списка из 15 случайных чисел от 0 до 90
print(list_15)

# 2.блок реализации пустой карточки для игры Лото
blank_karta = [['1', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
               ['-', '-', '-', '-', '-', '-', '-', '-', '9']]
for row in blank_karta:
    poz_in_lin = sorted(random.sample(range(1, 10), 5)) # генератор позиц (неповтор) в линии карты (range +1 не включая последний элемент)
    print('poz_in_lin;', poz_in_lin)
    for i in range(len(list_15[0:5])):
        print(f' инд в 5: {i}, знач из 15:{list_15[i]}, ном в лин:{poz_in_lin[i]}')
        #if list_15[i] in poz_in_lin:
            #blank_karta.remove(list_15[i])
    print(' '.join(str(elem) for elem in row)) #Вывод на экран карточки, используя генератора строки из списка через Join

print(poz_in_lin)

def get_list_index(blank_karta):
    for i, line in enumerate(blank_karta):
        print(i, line)
        if line[0] == '1' and line[-1] == '9':
            return i

list_index = get_list_index(blank_karta)
print('def', i)