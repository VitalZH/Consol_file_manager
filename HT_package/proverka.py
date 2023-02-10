import os
from os import path
import pickle

def def_list_dir():
    list_dir = os.listdir()
    return list_dir

while True:
    print('6 сохранить содержимое рабочей директории в файл')

    choice = input('Выберите пункт меню: ')
    if choice == '6':  # сохранить содержимое рабочей директории в файл
        print(f'запрос текущего состава директории: {def_list_dir()}')
        print(f'__print2_ {type(def_list_dir())}')
        if os.path.exists('fold_file_spis.txt'):
            with open('fold_file_spis.txt', 'rb') as f:
                fold_file = pickle.load(f)
                print(f'Принт проверка содержание файла на старте: {fold_file}')
        spis_papok = ''
        spis_file = ''
        for item in def_list_dir():
            if os.path.isdir(item) == True:
                spis_papok += item
            else:
                spis_file += item
        print(f'результат цикла разделения папок: {spis_papok}, и файлов {spis_file}')
        with open('fold_file_spis.txt', 'wb') as f:
            pickle.dump((spis_papok, spis_file), f)

    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')

