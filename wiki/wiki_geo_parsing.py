import mf2py
import json

def get_geo(doc):
    coords = []
    for d in doc['items']:
        try:
            data = {
                'name': d['properties']['adr'][0]['properties']['name'][0].split('\n')[0],
                'geo': d['properties']['geo'][0]['value']
            }
            coords.append(data)
        except (IndexError, KeyError):
            pass
    return coords


if __name__ == '__main__':
    url = input('Введите адрес страницы в wiki: ', )
    doc = mf2py.parse(url=url, html_parser='html5lib')

    with open('wiki_geo.json', 'w') as f:
        f.write(json.dumps(doc, indent=4))

    coords = get_geo(doc)
    for item in coords:
        print(item)
