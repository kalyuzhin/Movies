import requests

from bs4 import BeautifulSoup

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Safari/605.1.15'
}


def create_imdb_url(name: str) -> str:
    name = name.strip().replace(' ', '%20')
    return f'https://www.imdb.com/find/?q={name}&ref_=nv_sr_sm'


def parse_imdb_page(url: str) -> dict:
    result = dict()
    request = requests.get(url, headers=USER_AGENT).text
    soup = BeautifulSoup(request, 'html.parser')
    for elem in soup.find_all('div', class_='ipc-metadata-list-summary-item__tc'):
        elem = elem.find_next('a', class_='ipc-metadata-list-summary-item__t')
        result[f'{elem.text} ({elem.find_next("span").text})'] = f"https://www.imdb.com{elem.attrs['href']}".strip()
    return result
