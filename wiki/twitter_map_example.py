import folium

def make_map(map_file):
    # Пользовательская карта
    sample_map = folium.Map(location=[50, 5], zoom_start=17)
    
    # Маркер для Лондона
    london_marker = folium.Marker([51.5, -0.12], popup='London')
    london_marker.add_to(sample_map)
    
    # Маркер для Парижа
    paris_marker = folium.Marker([48.85, 2.35], popup='Paris')
    paris_marker.add_to(sample_map)
    
    # Сохранить в файл HTML
    sample_map.save(map_file)


if __name__ == '__main__':
    mapname = input('Enter map name: ', )
    make_map(mapname + '.html')
