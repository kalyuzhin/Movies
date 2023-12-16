import requests

from bs4 import BeautifulSoup


def create_imdb_url(name: str) -> str:
    name = name.strip().replace(' ', '%20')
    return f'https://www.imdb.com/find/?q={name}&ref_=nv_sr_sm'


def parse_imdb_page(url: str) -> dict:
    result = dict()
    request = requests.get(url).text
    soup = BeautifulSoup(request)
    for elem in soup.find_all('div', class_='ipc-metadata-list-summary-item__tc'):
        # elem.find_next("a", class_="ipc-metadata-list-summary-item__t").attrs["href"]
        elem = elem.find_next('a', class_='ipc-metadata-list-summary-item__t')
        result[f'{elem.text} ({elem.find_next("span").text})'] = f"https://www.imdb.com/{elem.attrs['href']}"
    return result
