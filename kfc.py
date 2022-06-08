import requests
import json

url = "https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true"
response = requests.get(url)
list_results = response.json()["searchResults"]
# with open('inf.json', 'w', encoding='utf8') as file:
#     json.dump(list_results, file, indent=4, ensure_ascii=False)
final_list = []

for i in list_results:
    if 'ru' in i['storePublic']['contacts']['streetAddress'] and type(i['storePublic']['contacts']['streetAddress']['ru']) == str:
        adress = i['storePublic']['contacts']['streetAddress']['ru'].split(', ')
        if adress[0].isdigit():
            adress.pop(0)
        adress = ', '.join(adress)
    else:
        adress = 'нет данных'
    latlon = ', '.join(map(str,i['storePublic']['contacts']["coordinates"]["geometry"]["coordinates"]))
    name = i['storePublic']["title"]['ru']
    phones = i['storePublic']['contacts']["phoneNumber"]
    if isinstance(i['storePublic']["openingHours"]["regular"]["startTimeLocal"], str):
        start = i['storePublic']["openingHours"]["regular"]["startTimeLocal"][:5]
        finish = i['storePublic']["openingHours"]["regular"]["endTimeLocal"][:5]
    else:
        start = 'нет данных'
        finish = 'нет данных'
    if i['storePublic']["openNow"]:
        openNow = ''
    else:
        openNow = " - closed"
    working_hours = 'пн - пт ' + start + '-' + finish + ', сб-вс ' + start + '-' + finish + openNow
    final_dict = {'adress': adress, 'latlon': latlon, 'name': name, "phones": phones, "working_hours": working_hours}
    final_list.append(final_dict)

with open('kfc.json', 'w', encoding='utf8') as file:
    json.dump(sorted(final_list, key=lambda x: x["adress"]), file, indent=4, ensure_ascii=False)

