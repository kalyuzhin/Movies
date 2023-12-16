import requests

from bs4 import BeautifulSoup


def create_kinopoisk_url(name: str) -> str:
    name = name.strip().replace(' ', '+')
    return f"https://www.kinopoisk.ru/index.php?kp_query={name}"


def parse_kinopoisk_page(url: str) -> dict:
    result = dict()
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'html.parser')
    try:
        match = soup.find('div', class_='search_results').find('div', class_='info').find('p', class_='name')
        result[match.text] = f"https://www.kinopoisk.ru{match.find('a').attrs['data-url']}"
        for element in match.find_next('div', class_='search_results').find_all('div', class_='info'):
            result[element.find_next('p',
                                     class_='name').text] = f"https://www.kinopoisk.ru{element.find_next('p', class_='name').find_next('a').attrs['data-url']}".strip()
    except Exception as ex:
        print("Error:\n", ex)

    return result
