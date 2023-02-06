'''
0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала;
1. Где это возможно переписать код с использованием генераторов и тернарных операторов;
2. Там где возможны исключительные ситуации добавить обработку исключений;
3. *Где это возможно применить декораторы.
'''
import shutil
import os
from os import getcwd
from os import mkdir
from os import rmdir
from os import walk
from os import path
import platform
import sys
import pickle

def def_list_dir():
    list_dir = os.listdir()
    return list_dir

def add_line():
    print('--' * 5, 'def_add_line', '--' * 5)

while True:
    add_line()
    print('1. создать папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('65 сохранить содержимое рабочей директории в файл')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории *необязательный пункт')
    print('12. выход')
    add_line()

    choice = input('Выберите пункт меню: ')
    if choice == '1':  # создать папку
        mk_dir = input('Внесите название создаваемой папки: ')
        '''было
        if not path.isdir(mk_dir):
            mkdir(mk_dir)
        else:
            print('Папка уже существует')
        '''
        mkdir(mk_dir) if not path.isdir(mk_dir) else print('Папка уже exists')

    elif choice == '2':  # удалить (файл/папку)
        rm_dir = input('Внесите название удаляемого файла\папки: ')
        try:
            rmdir(rm_dir)
        except FileNotFoundError:
            print('Файл отсуствует:')
        except NotADirectoryError:
            os.remove(rm_dir)

    elif choice == '3':  # копировать (файл/папку)
        copy_file = input('Введите имя копирумоей папки\файла: ')
        copy_newfile = input('Введите название новой папки\файла: ')
        shutil.copy(copy_file, copy_newfile)

    elif choice == '4':  # вывод всех объектов в рабочей папке
        print(def_list_dir())

    elif choice == '5':  # вывод только папок которые находятся в рабочей папке
        for item in def_list_dir():
            if os.path.isdir(item) == True:
                print(f'Перечень папок: {item}')

    elif choice == '6':  # вывод только файлов которые находятся в рабочей папке
        for item in def_list_dir():
            if os.path.isfile(item) == True:
                print(f'Перечень файлов: {item}')

    elif choice == '65':  # сохранить содержимое рабочей директории в файл
        print(f'запрос текущего состава директории: {def_list_dir()}')
        print(f'__print2_ {type(def_list_dir())}')
        if os.path.exists('fold_file_spis.txt'):
            with open('fold_file_spis.txt', 'rb') as f:
                fold_file = pickle.load(f)
                print(f'Принт проверка содержание файла на старте: {fold_file}')
        spis_papok = []
        spis_file = []
        for item in def_list_dir():
            if os.path.isdir(item) == True:
                spis_papok.append(item)
            else:
                spis_file.append(item)
        print(f'результат цикла разделения папок: {spis_papok}, и файлов {spis_file}')
        with open('fold_file_spis.txt', 'wb') as f:
            pickle.dump((spis_papok, spis_file), f)
            print(f'результат записи в файл fold_file_spis.txt папок: {spis_papok}, и файлов {spis_file}')

    elif choice == '7':  # просмотр информации об операционной системе
        print(f'Информация об ОС: {platform.platform()}')
        print(sys.platform)

    elif choice == '8':  # вывод информации о создателе программы
        print('Создатель программы: \nСтудент УИИ: Жуков В.А.')

    elif choice == '9':  # запуск игры викторина из предыдущего дз
        print('__________Игра Викторина__________')
        from HT_package.HT_9_victory import victory_9
        victory_9()

    elif choice == '10':  # запуск игры Счет из предыдущего дз
        print('__________Игра "Мой банковский счет"__________')
        from HT_package import HT_10_def_schet

    elif choice == '11':  # '11. смена рабочей директории *необязательный пункт'
        # Печать текущего рабочего каталога
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
        ch_dir = input('Введите путь для смены каталога')
        # Изменение текущего рабочего каталога
        os.chdir(ch_dir)
        # Печать текущего рабочего каталога
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))

    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
