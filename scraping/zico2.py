import json
import time
import requests
from bs4 import BeautifulSoup

start = time.time()

def get_soup(url):
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_links(count=1):
    zico_list = []
    soup = get_soup('https://www.ziko.pl/lokalizator/')
    tr_list = soup.find("tbody", class_="mp-pharmacies-table-elements clearfix").find_all("tr")
    for tr in tr_list:
        link = tr.find('td', class_="mp-table-access").find('a').get('href')
        link = 'https://www.ziko.pl/' + link
        zico_list.append(get_data(link))
        print(f'Записаны данные аптеки №{count}')
        count += 1
    with open('zico.json', 'w', encoding='utf8') as file:
        json.dump(zico_list, file, indent=4, ensure_ascii=False)


def get_data(link):
    soup = get_soup(link)
    coords = soup.find('div', class_="coordinates").find_all('span')
    try:
        latlon = [float(coords[0].text.strip().split(": ")[1]), float(coords[1].text.strip().split(": ")[1])]
    except:
        latlon = "no coordinates"
    list_data = soup.find('div', class_="leftdetailsbox").find_all('div')[:7]
    try:
        adress = ', '.join([i.find('span').text.strip() for i in list_data[1:3]])
    except:
        adress = "no address"
    try:
        name = list_data[0].find('span').text.strip()
    except:
        name = "no name"
    try:
        phones = list_data[4].find('a').text.strip().split(',')
    except:
        phones = "no phones"
    try:
        working_hours = []
        w_h = list_data[6].find_all('br')
        pon_pt ='pon-pt ' + w_h[0].previous_element.text.replace(' ', '')
        working_hours.append(pon_pt)
        sob = 'sob ' + w_h[5].previous_element.text.replace(' ', '')
        working_hours.append(sob)
        if len(w_h) > 6:
            nie = "nie " + w_h[6].previous_element.text.replace(' ', '')
            working_hours.append(nie)
    except:
        working_hours = "no working hours"
    zico_dict = {
        "adress": adress,
        "latlon": latlon,
        "name": name,
        "phones": phones,
        "working_hours": working_hours
    }
    return zico_dict


def main():
    get_links()
    finish = round(time.time() - start)
    print(f'Затрачено на работу парсера время: {finish} c')


if __name__ == "__main__":
    main()

