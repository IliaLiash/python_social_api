import networkx as nx

if __name__ == '__main__':
    g = nx.Graph()

    #Создаем узлы
    g.add_node('Путин', attrs={'имя': 'Владимир', 'возраст': 67})
    g.add_node('Песков', attrs={'имя': 'Дмитрий', 'возраст': 59})
    g.add_node('Ротенберг', attrs={'имя': 'Аркадий', 'возраст': 62})
    g.add_node('Абрамович', attrs={'имя': 'Роман', 'возраст': 55})

    #Создаем связи
    g.add_edge('Путин', 'Ротенберг', attrs={'Недвижимость': 'Дворец'})
    g.add_edge('Путин', 'Абрамович', attrs={'Бизнес': 'Сибнефть'})
    g.add_edge('Путин', 'Песков', attrs={'Работа': 'Кремль'})
    g.add_edge('Абрамович', 'Ротенберг', attrs={'Бизнес': 'Финансы'})

    print('Узлы: ', g.nodes())
    print('Связи: ', g.edges())
    print('Свзяь Путин - Ротенберг: ', g.has_edge('Путин', 'Ротенберг'))
