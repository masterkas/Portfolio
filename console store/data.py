price = {"Видеокарты": [["Palit GeForce RTX 3060 Dual", "12GB GDDR6","1320 MHz","15000 MHz", "123456", "2500.02 руб."], ["Palit GeForce RTX 3050 Dual", "8GB GDDR6","1550 MHz","14000 MHz", "134486", "1943.00 руб."],
['Gigabyte GeForce GTX 1660 Super OC', "6GB GDDR6","1530 MHz","14000 MHz", "469852", "1900.02 руб."]], "Процессоры": [["AMD Ryzen 1600", "AM4", "3.2GHz", "6", "456189", "850.21 руб."],
["AMD Ryzen 3600", "AM4", "3.6GHz", "6", "895647", "906.80 руб."], ['Intel Core i5-10400F', 'LGA1200', '2.9GHz', "6", '559846', '730.10 руб.']],
"Материнские платы": [["Gigabyte B450 Aorus Pro", "AMD AM4", "AMD B450", "4xDDR4", "954721", "321.90 руб."],["Gigabyte H410M H V3", "Intel LGA1200", "Intel H510", "2xDDR4", "963219", "224.22 руб."],
["ASUS TUF B450M-Pro Gaming", "AMD AM4", "AMD B450", "4xDDR4", "116548", "421.57 руб."]]}
recycle = []


def get_products():
    return price.keys()


def get_product(key):
    return price[key]


def add_recycle_bin(key_id, numbers):
    flag = True
    recycle_temp = []
    for i in price.values():
        for j in i:
            if key_id in j:
                flag = False
                recycle_temp.extend(j)
                break
        if flag == False:
            break
    while len(recycle_temp) > 3:
        recycle_temp.pop(1)
    recycle_temp.append(numbers)
    recycle.append(recycle_temp)


def get_recycle_bin():
    return recycle
def recycling_clear():
    recycle.clear()
    print("Ваша корзина пуста\n")


def search_name():
    return price.items()


