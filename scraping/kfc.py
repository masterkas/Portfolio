import requests
import json


def write_file(list_data):
    with open('kfc.json', 'w', encoding='utf8') as file:
        json.dump(list_data, file, indent=4, ensure_ascii=False)


def json_list():
    headers = {
        "accept": "text/html, application/xhtml + xml, application/xml;q = 0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true"
    response = requests.get(url=url, headers=headers)
    list_results = response.json()["searchResults"]
    return list_results


def get_data():
    kfc_list = []
    list_results = json_list()
    for i in list_results:
        try:
            name = i['storePublic']['title']['ru']
        except:
            name = "no name"
        try:
            address = i['storePublic']['contacts']['streetAddress']['ru']
        except:
            address = "not address"
        try:
            latlon = i['storePublic']['contacts']['coordinates']['geometry']['coordinates']
        except:
            latlon = 'no coordinates'
        try:
            phones = [i['storePublic']['contacts']['phone']['number']]
        except:
            phones = "no phones"
        try:
            w_h_start = i['storePublic']['openingHours']['regular']['startTimeLocal'][:-3]
            w_h_end = i['storePublic']['openingHours']['regular']['endTimeLocal'][:-3]
            working_hours = [f'пн-пт {w_h_start} до {w_h_end}', f'сб-вс {w_h_start} до {w_h_end}']
            if not i['storePublic']['openNow']:
                working_hours.append('closed')
        except:
            working_hours = 'no working_hours'

        kfc_dict = {
            "address": address,
            "latlon": latlon,
            "name": name,
            "phones": phones,
            "working_hours": working_hours
        }
        kfc_list.append(kfc_dict)
    return kfc_list


def main():
    write_file(get_data())


if __name__ == "__main__":
    main()


