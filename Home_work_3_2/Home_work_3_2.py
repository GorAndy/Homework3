# -*- coding='utf8' -*-
from urllib.parse import urlencode, urlparse
import requests

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = 00000000

# #Код для получения token
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


def make_list():
    """Оргинизует перебор друзей пользователя и определение их списков друзей"""
    list_my_friends = get_list_my_friends('')
    for friend in list_my_friends:
        friends_of_my_friend = get_list_my_friends(friend['id'])
        print_list_friends_of_friend(friend, friends_of_my_friend)


def print_list_friends_of_friend(friend, list_friends_of_friend):
    """Печатает last name и first name друзей выбранного друга"""
    print()
    print('Друзья моего друга {} {}:'.format(friend['first_name'], friend['last_name']))
    for _ in list_friends_of_friend:
        print('{} {}'.format(_['last_name'], _['first_name']))


def get_mutual_friends(source_uid, target_uid):
    """Поиск пересечений друзей двух пользователей"""
    params['source_uid'] = source_uid
    params['target_uid'] = target_uid
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    list_mutual_friends = response.json()['response']
    return list_mutual_friends


def search_user_by_id(user_id):
    """Определение данных пользователя по ID"""
    params['fields'] = 'nickname'
    params['user_ids'] = user_id
    response = requests.get('https://api.vk.com/method/users.get', params)
    user_name = response.json()['response'][0]
    return user_name


def print_2_user(user_id_1, user_id_2):
    """Шаблон для печати пары друзей"""
    user_1_name = search_user_by_id(user_id_1)
    user_2_name = search_user_by_id(user_id_2)
    print()
    print('Друг 1 {} {} и'.format(user_1_name['first_name'], user_1_name['last_name']))
    print('Друг 2 {} {}'.format(user_2_name['first_name'], user_2_name['last_name']))


def print_list_users(*user_id):
    """Шаблон для печати списка друзей"""
    user_name = search_user_by_id(user_id)
    print('Пользователь {} {}'.format(user_name['first_name'], user_name['last_name']))



token_url = "https://oauth.vk.com/blank.html#access_token=eb22aca4985d1bb2a475aa0894137d851e598bd78ca5062f32c7c01df242b4de3457&expires_in=86400&user_id=0000000"

o = urlparse(token_url)
fragments = dict(i.split('=') for i in o.fragment.split('&'))
access_token = fragments['access_token']
params = {
    'access_token': access_token,
           'v': VERSION,
        }


# Создаем списки друзей друзей
make_list()


list_my_friends = get_list_my_friends('')
list_id_my_friend = []

# Делаем список ID друзей
for friend in list_my_friends:
    list_id_my_friend.append(friend['id'])

# Проверяем общих друзей - каждого друга с каждым членом списка, исключаем проверку самого с собой
# Удаляем из списка совпадений основного пользователя.
for friend in list_id_my_friend:
    for i in range(len(list_id_my_friend)):
        if friend != list_id_my_friend[i]:
            intersection = []
            intersection += get_mutual_friends(friend, list_id_my_friend[i])
            for j in intersection:
                if int(fragments['user_id']) == j:
                    intersection.remove(int(fragments['user_id']))
            if len(intersection) != 0:
                print_2_user(friend, list_id_my_friend[i])
                print('Имеют общих друзей:')
                print_list_users(*intersection)
            else:
                print_2_user(friend, list_id_my_friend[i])
                print('НЕ Имеют общих друзей.')



