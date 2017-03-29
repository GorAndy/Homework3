# -*- coding='utf8' -*-
from urllib.parse import urlencode, urlparse
import requests
import json


def get_status(user_id=None):
    """Получение статуса пользователя"""
    if user_id:
        params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/status.get', params)
    print(response.json(), params)



AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = 5951940

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends, status, video',
    'v': VERSION,
}
print("?".join((AUTHORIZE_URL, urlencode(auth_data))))

token_url = "https://oauth.vk.com/blank.html#access_token=ada75321210bccf76cc06b1019be2badd6a639caedae3006dcde85fe28fd0e8e94bd3648d1e4d73e7e271&expires_in=86400&user_id=14414804"

o = urlparse(token_url)
fragments = dict(i.split('=') for i in o.fragment.split('&'))
access_token = fragments['access_token']

params = { 'access_token': access_token,
           'v': VERSION,
}



# get_status()
params['fields'] = 'nickname'
# params['user_id'] = '310351456'
response = requests.get('https://api.vk.com/method/friends.get', params)
print(response.json())
friends_list = response.json()['response']['items']
print('Мои друзья:')
friends_id_list = []
for friend in friends_list:
    friend.pop('online')
    friend.pop('nickname')
    friends_id_list.append(friend['id'])
    print('{} {}'.format(friend['last_name'], friend['first_name']))
print(friends_id_list)

# Поиск общих друзей friends.getMutual c параметрами target_uid или target_uids - список id через запятую
