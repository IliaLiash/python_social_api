from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    #Читает настройки и выполняет Twitter - аутентификацию. Возвращает tweepy.OAuthHandler
    api_key = ''
    api_secret_key = ''
    auth = OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
    return auth #Проходим аутентификацию

def get_twitter_client():
    #Создает клиент Twitter API и возращает его как объект
    auth = get_twitter_auth()
    client = API(auth)
    return client
