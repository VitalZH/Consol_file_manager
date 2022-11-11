
'''
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''

print('тек имя',__name__)
import random
# начало функции для проверки, ДЗ Тестирование функций
def get_random_person():
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушнин': '26.06.1799'}
    name, date = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, date
# окончание функции для проверки, ДЗ Тестирование функций
#№if __name__ == '__main__':

numbers = ['Пушкин А.С.', 'Лермонтов М.Ю.' , 'Гоголь Н.В.', 'Достоевский Ф.М.', 'Тургенев И.С.', 'Гончаров И.А.', 'Толстой Л.Н', 'Карамзин Н.М.', 'Гибоедов А.С.', 'Чехов А.П.']

friend = {
    'Пушкин А.С.': '06.06.1799',
    'Лермонтов М.Ю.': '15.10.1814',
    'Гоголь Н.В.': '01.04.1809',
    'Достоевский Ф.М.': '11.11.1821',
    'Тургенев И.С.': '09.11.1818',
    'Гончаров И.А.': '18.06.1812',
    'Толстой Л.Н': '09.09.1828',
    'Карамзин Н.М.': '12.12.1766',
    'Гибоедов А.С.': '15.01.1795',
    'Чехов А.П.': '29.01.1860'
}

right_dat = {
    'Пушкин А.С.': 'шестого июня 1799',
    'Лермонтов М.Ю.': 'пятнадцатого октября 1814',
    'Гоголь Н.В.': 'первого апреля 1809',
    'Достоевский Ф.М.': 'одиннадцатого ноября 1821',
    'Тургенев И.С.': 'девятого ноября 1818',
    'Гончаров И.А.': 'восемнадцатого июня 1812',
    'Толстой Л.Н': 'девятого сентября 1828',
    'Карамзин Н.М.': 'двенадцатого декабря 1766',
    'Гибоедов А.С.': 'пятнадцатого января 1795',
    'Чехов А.П.': 'двадцатьдевятого января 1860'
}
exit = 'yes'
while exit == 'yes' or exit == 'Yes': # запускаем основноей цикл программы
  result = random.sample(numbers, 5) # формируем список случайных ФИО
  print(result)
  count = 0 # отбнуляем счетчик правильных ответов
  for i in result: # запускаем цикл проверки ДР в выбранном списке
    print('введите дату рождения:', i, friend[i])
    data_check = input()
    if data_check == friend[i]:
      print('Отлично! дата верна.')
      count += 1 # счетчик правильных ответов
    else:
      print('Ответ неверен, правильная дата', right_dat[i])
  print('правильных ответов', count, 'из', len(result))
  exit = input('вы хотие продолжить Yes or No:')
else:
  print('end')