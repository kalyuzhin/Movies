import json

import requests

with open('config.txt') as config:
    TOKEN = config.readline().strip()
    MOVIE_PAGE = config.readline().strip()
    MOVIE_DATABASE = config.readline().strip()

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

BASE_URL = 'https://api.notion.com/v1'


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


def change_database_data(options: list) -> dict:
    if options[2] == 5:
        rating = 's|EI'
    elif options[2] == 4:
        rating = 'OFcy'
    elif options[2] == 3:
        rating = 'jNqD'
    elif options[2] == 2:
        rating = 'tjOu'
    elif options[2] == 1:
        rating = 'C>li'
    else:
        rating = 'bNBl'

    if options[1] == 'просмотрен':
        status = '9a7f810e-5ab8-4e58-aee6-afbe13d842c1'
    elif options[1] == 'хочу посмотреть':
        status = '49efec20-eaec-4cf5-9c9f-0bc0bdaeb0d0'
    else:
        status = '5ac495c5-c50b-451a-893a-7d6ad5bf0777'
    data = {
        'parent': {
            'type': 'database_id',
            'database_id': f'{MOVIE_DATABASE}'
        },
        'properties': {
            'Name': {
                'type': 'title',
                'title': [{'type': 'text', 'text': {'content': f'{options[0][0][:-5:]}'}}]
            },
            'Type': {
                'type': 'select',
                'select': {
                    'id': 'i`Sd'
                }
            },
            'Status': {
                'type': 'status',
                'status': {
                    'id': f'{status}'
                }
            },
            'Rating': {
                'type': 'select',
                'select': {
                    'id': f'{rating}'
                }
            },
            'Link': {
                'type': 'url',
                'url': f'{options[0][1]}'
            },
            'Year': {
                'type': 'number',
                'number': int(options[0][0][-4::])
            }
        }
    }
    return data


def add_to_database(data: dict) -> None:
    request = requests.post(BASE_URL + f'/databases/{MOVIE_DATABASE}/query', headers=HEADERS).text.find(
        data['properties']['Name']['title'][0]['text']['content'])
    if request != -1:
        print("Данный фильм уже есть в таблице")
        return
    else:
        request = requests.post(BASE_URL + f'/pages', headers=HEADERS, data=json.dumps(data))
        if request.status_code == 200:
            print('Успех')
        else:
            print("Error:\n", request.text)
