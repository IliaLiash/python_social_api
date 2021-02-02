import matplotlib.pyplot as plt
import numpy as np
import json

if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5])
    y = x * x
    plt.plot(x, y, 'r-')
    plt.axis([0, 6, 0, 30]) #Определяет видимый интервал
    plt.savefig('demo_plot.png')

    user_json = '{"user_id": "1", "name": "Marco"}'
    user_data = json.loads(user_json)   #Десериализует s (экземпляр str, содержащий документ JSON) в объект Python. Здесь экземпляр - user_json.
    print(user_data['name'])

    user_data['Languages'] = ['Python']
    user_json = json.dumps(user_data, indent=4, ensure_ascii=False) #Сериализует obj в строку JSON-формата.
    print(user_json)