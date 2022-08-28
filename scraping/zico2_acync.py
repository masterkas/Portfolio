import json
import time
from bs4 import BeautifulSoup
import aiohttp
import asyncio


async def get_soup(session, url):
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    response = await session.get(url=url, headers=headers)
    soup = BeautifulSoup(await response.text(), 'lxml')
    return soup


async def get_data(link, session, count, number):
    soup = await get_soup(session, link)
    coords = soup.find('div', class_="coordinates").find_all('span')
    try:
        latlon = [float(coords[0].text.strip().split(": ")[1]), float(coords[1].text.strip().split(": ")[1])]
    except:
        latlon = "no coordinates"
    list_data = soup.find('div', class_="leftdetailsbox").find_all('div')[:7]
    try:
        address = ', '.join([i.find('span').text.strip() for i in list_data[1:3]])
    except:
        address = "no address"
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
        pon_pt = 'pon-pt ' + w_h[0].previous_element.text.replace(' ', '')
        working_hours.append(pon_pt)
        sob = 'sob ' + w_h[5].previous_element.text.replace(' ', '')
        working_hours.append(sob)
        if len(w_h) > 6:
            nie = "nie " + w_h[6].previous_element.text.replace(' ', '')
            working_hours.append(nie)
    except:
        working_hours = "no working hours"
    zico_dict = {
        "address": address,
        "latlon": latlon,
        "name": name,
        "phones": phones,
        "working_hours": working_hours
    }
    zico_list.append(zico_dict)
    print(f'[INFO] - добавлена {count} аптека из {number}')


async def get_links(url):
    async with aiohttp.ClientSession() as session:
        count = 1
        soup = await get_soup(session, url)
        tr_list = soup.find("tbody", class_="mp-pharmacies-table-elements clearfix").find_all("tr")
        tasks = []
        for tr in tr_list:
            link = tr.find('td', class_="mp-table-access").find('a').get('href')
            link = 'https://www.ziko.pl/' + link
            task = asyncio.create_task(get_data(link, session, count, len(tr_list)))
            tasks.append(task)
            count += 1
        await asyncio.gather(*tasks)


def main():
    start = time.time()
    url = 'https://www.ziko.pl/lokalizator/'
    asyncio.run(get_links(url))
    with open('zico.json', 'w', encoding='utf8') as file:
        json.dump(zico_list, file, indent=4, ensure_ascii=False)
    finish = round(time.time() - start)
    print(f'Затрачено на работу парсера время: {finish} c.')


if __name__ == "__main__":
    zico_list = []
    main()
