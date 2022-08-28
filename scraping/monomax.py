import json
import requests
from bs4 import BeautifulSoup


def write_file(list_data):
    with open('monomax.json', 'w', encoding='utf8') as file:
        json.dump(list_data, file, indent=4, ensure_ascii=False)


def get_soup():
    url = 'https://monomax.by/map'
    headers = {
        "accept": "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_latlon():
    latlon = []
    soup = get_soup()
    r = soup.find_all("script", type="text/javascript")[-1].text.replace(' ','').split('\n')
    for element in r:
        if element != '' and element[0] == '[':
            coordinates = element[1:-2].split(',')
            for i in range(len(coordinates)):
                coordinates[i] = float(coordinates[i])
            latlon.append(coordinates)
    return latlon


def get_data(count=0):
    latlon = get_latlon()
    monomax_list = []
    soup = get_soup()
    list_shop = soup.find('div', class_="all-shops").find_all('div', class_='shop')
    for shop in list_shop:
        try:
            address = shop.find(class_="name").text
            if address[-1] == ',':
                address = address[:-1]
        except:
            address = 'нет адреса'

        try:
            phones = []
            phones_list = shop.find_all(class_="phone")
            for ph in phones_list:
                phone = ph.find('a').text
                if phone != '':
                    for element in phone[1:]:
                        if not element.isdigit():
                            phone = phone.replace(element, '')
                    phones.append(phone)
        except:
            phones = 'нет телефона'

        monomax_dict = {
            "address": address,
            "latlon": latlon[count],
            "name": "Мономах",
            "phones": phones,
        }
        monomax_list.append(monomax_dict)
        count += 1
    return monomax_list


def main():
    write_file(get_data())


if __name__ == "__main__":
    main()
