# -*- coding='utf8' -*-
from urllib.parse import urlencode, urlparse
import requests

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = 5951940

# Код для получения token
# auth_data = {
#     'client_id': APP_ID,
#     'display': 'mobile',
#     'response_type': 'token',
#     'scope': 'friends, status, video',
#     'v': VERSION,
# }
#
# print("?".join((AUTHORIZE_URL, urlencode(auth_data))))


def get_list_my_friends(user_id):
    """Создаем словарь с данными друзей пользователя с указанным в аргументе id"""
    params['fields'] = 'nickname'
    params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_list = response.json()['response']['items']
    return friends_list


def print_list_friends_of_friend(friend_fn, friend_ln, list_friends_of_friend):
    """Печатает last name и first name друзей выбранного друга"""
    print()
    print('Друзья моего друга {} {}:'.format(friend_fn, friend_ln))
    for _ in list_friends_of_friend:
        print('{} {}'.format(_['last_name'], _['first_name']))


def get_mutual_friends(source_uid, target_uid):
    """Поиск пересечений друзей двух пользователей"""
    params['source_uid'] = source_uid
    params['target_uid'] = target_uid
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    print('Общие друзья с моими друзьями')
    list_mutual_friends = response.json()['response']
    return list_mutual_friends


def search_friend_by_id(user_id):
    """Поиск друга в списке по id"""
    for friend in list_my_friends:
        if int(user_id) == int(friend['id']):
            first_name = friend['first_name']
            last_name = friend['last_name']
    return first_name, last_name


token_url = "https://oauth.vk.com/blank.html#access_token=c67e848665a395737b1b9ac0d2e7e86983844a44cceb4355998b22f9cb820b075cf06f40e13f478ddcc01&expires_in=86400&user_id=14414804"

o = urlparse(token_url)
fragments = dict(i.split('=') for i in o.fragment.split('&'))
access_token = fragments['access_token']

params = {
    'access_token': access_token,
           'v': VERSION,
        }

list_my_friends = get_list_my_friends('')
list_id_of_my_friends = []
for friend in list_my_friends:
    friends_of_my_friend = get_list_my_friends(friend['id'])
    # print_list_friends_of_friend(friend['first_name'], friend['last_name'], friends_of_my_friend)
    list_id_of_my_friends.append(friend['id'])

print(list_id_of_my_friends)
# get_mutual_friends(list_id_of_my_friends)
print(get_mutual_friends('', '2857935'))
# print(search_friend_by_id())





# Поиск общих друзей friends.getMutual c параметрами target_uid или target_uids - список id через запятую
