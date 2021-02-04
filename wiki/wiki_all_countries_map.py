import mf2py
import folium
import csv
import json
from folium.plugins import MarkerCluster

def get_geo(doc):   #Принимает словарь и возвращает список словарй
    for d in doc['items']:
        try:
            data = {
                'name': d['properties']['adr'][0]['properties']['name'][0].split('\n')[0],
                'geo': d['properties']['geo'][0]['value']
            }
            return data
        except:
            pass

def make_map(map_file, data):
    sample_map = folium.Map(location=[50, 5], zoom_start=2)
    # Добавляем кластер для группировки маркеров
    marker_cluster = MarkerCluster().add_to(sample_map)
    for element in data:
        # Создаем маркеры и добавляем их в кластер, уже соединенный с картой
        try:
            team_marker = folium.Marker([element['geo'].split(';')[0], element['geo'].split(';')[1]], popup=element['name'])
            team_marker.add_to(marker_cluster)
        except:
            pass

    # Сохранить в файл HTML
    sample_map.save(map_file)

if __name__ == '__main__':
    countries_data = []
    with open('country_list.txt', 'r') as f:
        countries_list = f.readlines()
        countries_list = [country[:-2].replace("'",'').replace(' ','') for country in countries_list]
        for country in countries_list:
            url = str('https://en.wikipedia.org/wiki/' + str(country))
            doc = mf2py.parse(url=url, html_parser='html5lib')
            coords = get_geo(doc)   #Передаем словарь в функцию
            if coords:
                countries_data.append(coords)

    with open('countries.json', 'a') as f:
        try:
            json.dump(countries_data, f)
        except:
            pass

    with open('countries.txt', 'a') as f:
        for element in countries_data:
            try:
                f.write(str(element) + '\n')
            except:
                pass


    with open("countries.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(countries_data[0].keys())
        for dict_item in countries_data:
            try:
                csv_writer.writerow(dict_item.values())
            except:
                pass

    make_map('wiki_countries.html', countries_data)
