import data, copy
from decimal import Decimal


def get_list():
    list_products = [i for i in data.get_products()] + ['Вернуться в меню']
    return list_products


def get_list_products():
    list_products = get_list()
    return '\n'.join([f'{i+1}. {list_products[i]}' for i in range(len(list_products))])


def sort_tabl(tabl, key):
    header = {0: ['наименование товара', 'код товара', 'цена', 'количество'], 1: ['модель', 'память', 'базовая частота', 'частота памяти', 'код товара', 'цена'], 2: ['модель', 'сокет', 'частота', 'количество ядер', 'код товара', 'цена'],
    3: ['модель', 'сокет', 'чипсет', 'память', 'код товара', 'цена']}
    if key != 0:
        tabl.append(['Вернуться в меню'])
    else:
        tabl.append(['ИТОГО'])
    tabl.insert(0, header[key])
    if sum([len(i) for i in tabl[0]]) == sum([len(i) for i in tabl[-2]]):
        tabl[0][0] = tabl[0][0] + ' '
    while sum([len(i) for i in tabl[0]]) != sum([len(i) for i in tabl[-2]]):
        for i in range(len(tabl) - 2):
            for j in range(len(tabl[i])):
                if len(tabl[i][j]) > len(tabl[i+1][j]):
                    tabl[i+1][j] = tabl[i+1][j] + ' '*(len(tabl[i][j]) - len(tabl[i+1][j]))
                else:
                    tabl[i][j] = tabl[i][j] + ' '*(len(tabl[i+1][j]) - len(tabl[i][j]))


def print_model(list_model):
    counter = -1
    indent = 8
    space = sum([len(i) for i in list_model[0]])+(len(list_model[0])-1)*indent + 3
    for i in list_model:
        counter += 1
        print(f'{counter}. ' if counter > 0 else ' ' * 3, end='')
        print(*i, sep=(' '* indent))
        print('-' * space)


def id_model(list_model):
    id_products = []
    for i in list_model:
        if len(i) > 1:
            id_products.append((i[-2]).strip())
    return id_products


def get_product(key):
    list_products = get_list()
    try:
        if len(list_products) < int(key) or int(key) < 1:
            raise IndexError
    except IndexError:
        return ("Такой категории не существует.\nВы должны ввести номер(цифру) категории или выбрать последний пункт для возврата в меню.\n", False)
    except:
        return ("Такой категории не существует.\nВы должны ввести номер(цифру) категории или выбрать последний пункт для возврата в меню.\n", False)
    if len(list_products) == int(key):
        return key
    else:
        models = copy.deepcopy(data.get_product(list_products[int(key)-1]))
        sort_tabl(models, int(key))
        id_products = id_model(models)
        print_model(models)
    models.clear()
    return id_products


def add_recycle(key_id, numbers):
    data.add_recycle_bin(key_id, numbers)
    return "Товар успешно добавлен в корзину.\n"


def get_recycle():
    indent = 8
    recycle = data.get_recycle_bin()
    if recycle == []:
        return ['Ваша корзина пуста.\n']
    else:
        recycle_bin = copy.deepcopy(recycle)
        sort_tabl(recycle_bin, 0)
        space = sum([len(i) for i in recycle_bin[0][:2]]) - len(recycle_bin[-1][0])
        recycle_bin[-1][0] = recycle_bin[-1][0] +' '*(space+indent)
        total = 0
        for i in range(1, len(recycle_bin)-1):
            total = Decimal(str(total)) + Decimal((recycle_bin[i][2].split(' '))[0])*int(recycle_bin[i][-1])
        recycle_bin[-1].append(str(total) + ' руб.')
        print_model(recycle_bin)
        return recycle_bin[-1][-1]


def searc_inquiry(inquiry, list_name=[]):
    validation = validation_search(inquiry)
    if validation:
        return ("Длина запроса должна быть не менее 4-ех символов.\n", False)
    list_products = get_list()
    res = data.search_name()
    for k, v in res:
        for j in v:
            if j[0].find(inquiry) != -1:
                list_name.append(copy.deepcopy(j))
                key = k
    if list_name == []:
        return "Товар не найден. Повторите запрос или воспользуйтесь каталогом.\n"
    sort_tabl(list_name, (list_products.index(key)+1))
    id_products = id_model(list_name)
    print_model(list_name)
    list_name.clear()
    return id_products


def validation_search(inquiry):
    try:
        if len(inquiry) < 4:
            raise IndexError
    except IndexError:
        return True
