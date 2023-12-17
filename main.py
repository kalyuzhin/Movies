from parsers import *
from notion import *


def main() -> None:
    name = input("Введите название фильма или сериала:\n")
    service = input("Введите, где хотите найти его(кинопоиск или imdb):\n")
    if service.strip().lower() == 'кинопоиск':
        result = kinopoisk_functions.parse_kinopoisk_page(kinopoisk_functions.create_kinopoisk_url(name))
    elif service.strip().lower() == 'imdb':
        result = imdb_functions.parse_imdb_page(imdb_functions.create_imdb_url(name))
    else:
        print('Ошибка!')
        exit()
    i = 1
    for elem in result:
        print(f'\t{i}.{elem} - {result[elem]}')
        i += 1
    print("Выберите нужный вам элемент(скопируйте и вставьте его название):\n")
    name = input()
    print("Вы хотите его посмотреть или вы уже его просмотрели?:\n")
    choice = input()
    if choice.strip().lower() == 'хочу посмотреть':
        notion.want_to_watch(notion.change_data(result, name))
    elif choice.strip().lower() == 'просмотрен':
        notion.already_watched(notion.change_data(result, name))


if __name__ == '__main__':
    main()
