import bus_log
from data import recycling_clear


def show_data(data):
    print(data)


def show_query(message):
    return input(message)


def show_catalog():
    catalog = bus_log.get_list_products()
    show_data(catalog)
    return


def choose_product(key):
    res = bus_log.get_product(key)
    return res


def add_recycle(key_id, numbers):
    res = bus_log.add_recycle(key_id, numbers)
    show_data(res)


def show_recycle():
    res = bus_log.get_recycle()
    if isinstance(res, list):
        show_data(*res)
    return res


def search(inquiry):
    res = bus_log.searc_inquiry(inquiry)
    if isinstance(res, tuple):
        show_data(res[0])
        inquiry = show_query("Введите название товара (минимум 4 символа):\n")
        search(inquiry)
    elif isinstance(res, str):
        show_data(res)
        menu()
    else:
        submenu(res)


def menu():
    show_data("Добро пожаловать в наш магазин.")
    while True:
        choose_operation = show_query("""Пожалуйста выберите номер операции:
1. Выход
2. Показать каталог товаров
3. Корзина
4. Поиск по названию товара\n""")
        if choose_operation == '1':
            show_data('Спасибо, что посетили наш магазин.')
            break
        elif choose_operation == '2':
            second_menu()
        elif choose_operation == '3':
            third_menu()
        elif choose_operation == '4':
            inquiry = show_query("Введите название товара (минимум 4 символа):\n")
            search(inquiry)
        else:
            show_data("Такой операциии не существует.\nВы должны ввести номер(цифру) существующей операции.\n")
            continue
        break


def second_menu():
    show_data("Выберите категорию товара или вернитесь в меню:")
    show_catalog()
    choose_operation = show_query("")
    res = choose_product(choose_operation)
    if isinstance(res, tuple):
        show_data(res[0])
        second_menu()
    elif res == choose_operation:
        return menu()
    else:
        submenu(res)


def submenu(res):
    choose_model = show_query("Добавте нужную модель в корзину или вернитесь в меню выбора категорий:\n")
    if choose_model.isdigit() == True and  0 < int(choose_model) <= len(res):
        if int(choose_model) == len(res):
            second_menu()
        else:
            while True:
                numbers = show_query('Укажите количество(не более 10 штук за одну покупку):\n')
                if numbers.isdigit() == True and 0 < int(numbers) <= 10:
                    break
                else:
                    show_data("Введите корректные данные.")
            add_recycle(res[int(choose_model)], numbers)
            while True:
                choose_operation = show_query('1. Продолжить покупки\n2. Перейти к оформлению заказа\n')
                if choose_operation == '1':
                    second_menu()
                elif choose_operation == '2':
                    third_menu()
                else:
                    show_data("Такой операциии не существует.\nВы должны ввести номер(цифру) существующей операции.\n")
                    continue
                break
    else:
        show_data("Укажите корректно номер(цифру) модели или выберите последний пункт для возврата в меню.\n ")
        submenu(res)


def third_menu():
    res = show_recycle()
    if isinstance(res, list):
        menu()
    else:
        while True:
            choose_operation = show_query('1. Оформить заказ\n2. Продолжить покупки\n3. Очистить корзину\n')
            if choose_operation == '1':
                show_data(f'Ваш заказ на сумму {res} подтвержден. Спасибо за покупку.')
                break
            elif choose_operation == '2':
                second_menu()
            elif choose_operation == '3':
                recycling_clear()
                menu()
            else:
                show_data("Такой операциии не существует.\nВы должны ввести номер(цифру) существующей операции.\n")
                continue
            break