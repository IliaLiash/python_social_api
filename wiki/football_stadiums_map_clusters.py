import folium
import pandas as pd
from folium.plugins import MarkerCluster


url = 'https://raw.githubusercontent.com/jokecamp/FootballData/master/other/stadiums-with-GPS-coordinates.csv'

#Получаем координаты футбольных полей
data = pd.read_csv(url)
data = data[['Team', 'Latitude', 'Longitude']]
data = data.values.tolist()

def make_map(map_file, data):
    sample_map = folium.Map(location=[50, 5], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(sample_map)     #Добавляем кластер для группировки маркеров
    for element in data:
        #Создаем маркеры и добавляем их в кластер, уже соединенный с картой
        team_marker = folium.Marker([element[1], element[2]], popup=element[0])
        team_marker.add_to(marker_cluster)

    # Сохранить в файл HTML
    sample_map.save(map_file)


if __name__ == '__main__':
    mapname = str('FA Premier')
    make_map(mapname + '.html', data)