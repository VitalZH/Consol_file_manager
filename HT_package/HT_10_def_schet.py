schet = 0
story_cost = []
story_name = []


# объявляем функцию для пополнения cчета " условие if == '1' "

def schet_def():  # пополнение счета
    global schet
    sum_add = ''  # input('Внесите сумму для пополнеия счета: ')
    while not sum_add.isdigit():
        sum_add = input('Внесите сумму для пополнеия счета: ')
    sum_add = int(sum_add)
    schet += sum_add
    return schet


def buy_def2():  # совершение покупки
    global story_cost
    global story_name
    global schet
    buy_cost = ''  # проверка стоимости покуки
    while not buy_cost.isdigit():
        buy_cost = input('Внесите СТОИМОСТЬ покупки: ')
    buy_cost = int(buy_cost)
    if buy_cost > schet:
        print('Недостаточно средств на счете, пополните счет')

    else:  # ввод стоимость покуки
        buy_name = input('Внесите НАЗВАНИЕ покупки: ')
        schet = schet - buy_cost
        story_cost.append(buy_cost)
        story_name.append(buy_name)
        print(f'остаток счета: {schet}')
        return buy_name, buy_cost


def hist_def3():  # история покупок
    global story_cost
    global story_name
    dict_buy = dict(zip(story_name, story_cost))
    return dict_buy


while True:
    print('-----------------------------\nВыберите пункт меню 1-4')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('Выберите пункт меню: ')
    print('------------------------------')

    if choice == '1':
        schet_if1 = schet_def()
        print(f'текущий счет: {schet_if1}')

    elif choice == '2':
        purchase = buy_def2()
        print(f'покупка совершена: {purchase}')

    elif choice == '3':  # история покупок
        print(f'стоимость покупок: {story_cost}')
        print(f'название покупок: {story_name}')
        buy_history = hist_def3()
        print(f'формируем словарь покупок: {buy_history}')

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
print('end')
print(f'финальный счет: {schet}')