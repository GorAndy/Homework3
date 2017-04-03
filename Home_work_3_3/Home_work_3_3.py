import requests
import os.path
import glob

YANDEX_KEY = 'trnsl.1.1.20170402T171942Z.f25d4d25bbbb0e64.25775e365f685552b1819fe5a70a43ea3f0dbb47'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def find_file(path):
    """Выборка входных файлов в список"""
    list_files = glob.glob(os.path.join(path, '??.txt'))
    return list_files


def translate_file(file_in):
    with open(file_in) as f:
        file_read_in = f.read()
    response = requests.get(URL, params={'key': YANDEX_KEY, 'text': file_read_in, 'lang': lang_out})
    text_out = ''.join(response.json()['text'])
    return text_out


def wrire_out(text_out):
    file_out = os.path.join(path_out, 'file_out.txt')
    with open(file_out, 'a') as f:
        f.write(text_out)


# указать путь к каталогу с файлами, которые нужно перевести
path_in = ''
# Указать путь к файлу с результатом перевода
path_out = ''
# Указать язык на который нужно перевести (исходный язык определится автоматически)
lang_out = 'ru'

list_files = find_file(path_in)
for file_in in list_files:
    text_out = translate_file(file_in)
    wrire_out(text_out)