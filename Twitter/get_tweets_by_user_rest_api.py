import os
import json
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor

def get_twitter_auth():
    #Читает настройки и выполняет Twitter - аутентификацию. Возвращает tweepy.OAuthHandler
    api_key = '7knZAhWlRctlzMfaa35MQQgy4'
    api_secret_key = 'hcI6UuHZOOyffRzJ63eHJRr0qmkGLLCv7BGQ8dPzg5tdR0jaSG'
    auth = OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
    return auth #Проходим аутентификацию

def get_twitter_client():
    #Создает клиент Twitter API и возращает его как объект
    auth = get_twitter_auth()
    client = API(auth)
    return client

if __name__ == '__main__':
    client = get_twitter_client()
    user = input('Enter Twitter user: ', )

    fname = 'user_twits_{}.json'.format(user)
    if not os.path.exists(fname):  # Если файла не существует - создаем
        with open(fname, 'w') as f:
            for page in Cursor(client.user_timeline,
                           screen_name = user,
                           count = 200).pages(16):
                for status in page:
                    f.write(json.dumps(status._json)+'\n')
    else:
        with open(fname, 'r') as f:
            i = 1
            for line in f:
                tweet = json.loads(line)
                print(str(i), tweet['text'], sep=' ')
                i += 1