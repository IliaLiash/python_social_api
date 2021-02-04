import os
import sys
import json
import time
import math
from tweepy import Cursor
from twitter_client import get_twitter_client

MAX_FRIENDS = 2532900

def paginate(items, n):
    """Сгенерировать из элементов блоки размера n"""
    for i in range(0, len(items), n):
        yield items[i:i+n]

if __name__ == '__main__':
    screen_name = input('Enter Twitter account: ', )
    client = get_twitter_client()
    dirname = "users/{}".format(screen_name)
    max_pages = math.ceil(MAX_FRIENDS / 5000)
    try:
        os.makedirs(dirname, mode=0o755, exist_ok=True)
    except OSError:
        print("Каталог {} уже существует".format(dirname))
    except Exception as e:
        print("Ошибка при создании каталога {}".format(dirname))
        print(e)
        sys.exit(1)

    # получить читателей для конкретного пользователя
    fname = "users/{}/followers.jsonl".format(screen_name)
    with open(fname, 'w') as f:
        for followers in Cursor(client.followers_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(followers, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    f.write(json.dumps(user._json)+"\n")
            if len(followers) == 5000:
                print("Есть еще результаты. 60-сек. режим сна, чтобы избежать ограничения на частоту запросов")
                time.sleep(60)

    # получить друзей для конкретного пользователя
    fname = "users/{}/friends.jsonl".format(screen_name)
    with open(fname, 'w') as f:
        for friends in Cursor(client.friends_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(friends, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    f.write(json.dumps(user._json)+"\n")
            if len(friends) == 5000:
                print("Есть еще результаты. 60-сек. режим сна, чтобы избежать ограничения на частоту запросов")
                time.sleep(60)

    # получить профиль пользователя
    fname = "users/{}/user_profile.json".format(screen_name)
    with open(fname, 'w') as f:
        profile = client.get_user(screen_name=screen_name)
        f.write(json.dumps(profile._json, indent=4))
        followers_count = profile.followers_count
        friends_count = profile.friends_count
        print(f'Followers: {followers_count}')
        print(f'Friends: {friends_count}')
