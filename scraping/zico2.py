import requests, json
from bs4 import BeautifulSoup

url = 'https://www.ziko.pl/lokalizator/'
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
req = requests.get(url, headers)
src = req.text
soup = BeautifulSoup(src, 'lxml')
common_list = soup.find(class_="mp-pharmacies-table-elements clearfix").findAll("tr")
final_list = []
count = 1
for i in common_list:
    print(f'{count} адресс запиысвается, ждите...')
    name = i.find(class_="mp-table-dermo").find(class_="mp-pharmacy-head").text.strip()
    working_hours_all = i.find(class_="mp-table-hours").findAll("span")
    working_hours = []
    for j in range(0, len(working_hours_all), 2):
        a = working_hours_all[j].text + working_hours_all[j + 1].text
        working_hours.append(a)
    link = "https://www.ziko.pl" + i.find(class_="mp-table-access").find('a').get('href')
    req = requests.get(link, headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    data_list = soup.find(class_="leftdetailsbox").findAll("div")
    address = data_list[1].find('span').text.strip() + ', ' + data_list[2].find('span').text.strip()
    phone = [data_list[4].find("a").text.strip()]
    coordinates = soup.find(class_="coordinates").findAll("span")
    with_geo = (coordinates[0].text.strip()).split(' ')[-1]
    long_geo = (coordinates[1].text.strip()).split(' ')[-1]
    latlon = [with_geo, long_geo]
    common_dict = {
        "address": address,
        'latlon': latlon,
        'name': name,
        "phones": phone,
        "working_hours": working_hours

    }
    final_list.append(common_dict)
    print('Готово')
    count += 1

with open('zico.json', 'w', encoding='utf8') as file:
    json.dump(final_list, file, indent=4, ensure_ascii=False)
