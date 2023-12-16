import json

import requests

from parsers import *

with open('config.txt') as config:
    TOKEN = config.readline().strip()
    MOVIE_PAGE = config.readline().strip()

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# DATA = {
#     'children': [
#         {
#             'object': 'block',
#             'type': 'bookmark',
#             'bookmark': {
#                 'caption': [{"type": "text", "text": {"content": f"Американский психопат"}}],
#                 'url': f'https://www.kinopoisk.ru/film/588'
#
#             }
#         }
#     ]
# }

BASE_URL = 'https://api.notion.com/v1'


# request = requests.get(BASE_URL + f"/blocks/{MOVIE_PAGE}/children", headers=HEADERS).json()
#
# while request['results'][0]['type'] != 'column':
#     request = requests.get(BASE_URL + f"/blocks/{request['results'][0]['id']}/children", headers=HEADERS).json()
#
# try:
#     request = requests.patch(
#         BASE_URL + f"/blocks/{request['results'][1]['id']}/children", headers=HEADERS, data=json.dumps(DATA))
#     if request.status_code == 200:
#         print('Done...')
#     else:
#         print(request.text)
# except Exception as ex:
#     print('Error!!!\n', ex)


def already_watched(data: dict) -> None:
    try:
        request = requests.get(BASE_URL + f"/blocks/{MOVIE_PAGE}/children", headers=HEADERS).json()
        while request['results'][0]['type'] != 'column':
            request = requests.get(BASE_URL + f"/blocks/{request['results'][0]['id']}/children", headers=HEADERS).json()
        request = requests.patch(
            BASE_URL + f"/blocks/{request['results'][1]['id']}/children", headers=HEADERS, data=json.dumps(data))
        if request.status_code == 200:
            print('Done...')
        else:
            print(request.text)
    except Exception as ex:
        print('Ошибка!!!\n', ex)


def want_to_watch(data: dict) -> None:
    try:
        request = requests.get(BASE_URL + f"/blocks/{MOVIE_PAGE}/children", headers=HEADERS).json()
        while request['results'][0]['type'] != 'column':
            request = requests.get(BASE_URL + f"/blocks/{request['results'][0]['id']}/children", headers=HEADERS).json()
        request = requests.patch(
            BASE_URL + f"/blocks/{request['results'][0]['id']}/children", headers=HEADERS, data=json.dumps(data))
        if request.status_code == 200:
            print('Done...')
        else:
            print(request.text)
    except Exception as ex:
        print('Ошибка!!!\n', ex)


def change_data(dic: dict, name: str) -> dict:
    data = {
        'children': [
            {
                'object': 'block',
                'type': 'bookmark',
                'bookmark': {
                    'caption': [{"type": "text", "text": {"content": f"{name}"}}],
                    'url': f'{dic[name]}'
                }
            }
        ]
    }
    return data
