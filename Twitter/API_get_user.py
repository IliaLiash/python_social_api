from twitter_client import get_twitter_client
import json
client = get_twitter_client()
profile = client.get_user(screen_name='navalny')
print(json.dumps(profile._json, indent=4))
followers_count = profile.followers_count
friends_count = profile.friends_count
print(f'Followers: {followers_count}')
print(f'Friends: {friends_count}')
