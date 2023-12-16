import requests

from bs4 import BeautifulSoup


def create_imdb_url(name: str) -> str:
    name = name.strip().replace(' ', '%20')
    return f'https://www.imdb.com/find/?q={name}&ref_=nv_sr_sm'


