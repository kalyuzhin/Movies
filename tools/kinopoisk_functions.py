import requests

from bs4 import BeautifulSoup


def create_kinopoisk_url(name: str) -> str:
    name = name.strip().replace(' ', '+')
    return f"https://www.kinopoisk.ru/index.php?kp_query={name}"


