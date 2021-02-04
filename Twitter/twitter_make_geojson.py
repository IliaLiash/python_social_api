import json

if __name__ == '__main__':
    tweets = input('Input file name: ', )
    # Прочесть коллекцию твитов и построить структуру геоданных
    with open(tweets, 'r') as f:
        geo_data = {
            "type": "FeatureCollection",
            "features": []
        }
        for line in f:
            tweet = json.loads(line)
            try:
                if tweet['coordinates']:
                    geo_json_feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": tweet['coordinates']['coordinates']
                        },
                        "properties": {
                            "text": tweet['text'],
                            "created_at": tweet['created_at']
                        }
                    }
                    geo_data['features'].append(geo_json_feature)
            except KeyError:
                # пропустить, если документ json 
                # не является твитом (ошибки и пр.)
                continue
     
    # Сохранить геоданные
    with open('geojson.json', 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
