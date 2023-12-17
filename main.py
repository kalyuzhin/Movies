from parsers import *
from notion import *


def main() -> None:
    name = input("Введите название фильма или сериала:\n")
    service = input("Введите, где хотите найти его(кинопоиск или imdb):\n")
    if service.strip().lower() == 'кинопоиск':
        items = kinopoisk_functions.parse_kinopoisk_page(kinopoisk_functions.create_kinopoisk_url(name))
    elif service.strip().lower() == 'imdb':
        items = imdb_functions.parse_imdb_page(imdb_functions.create_imdb_url(name))
    else:
        print('Ошибка!')
        exit()
    i = 1
    for elem in items:
        print(f'\t{i}.{elem} - {items[elem]}')
        i += 1
    print("Выберите нужный вам элемент(скопируйте и вставьте его название):")
    name = input()
    item = next((k, v) for k, v in items.items() if k == name)
    print("Вы хотите его посмотреть или вы уже его просмотрели?:")
    choice = input().strip().lower()
    if choice == 'хочу посмотреть':
        # notion.want_to_watch(notion.change_data(result, name))
        notion.add_to_database(notion.change_database_data([item, choice, 0]))
    elif choice == 'просмотрен':
        # notion.already_watched(notion.change_data(result, name))
        rating = int(input("Как вы оцените этот фильм по пятибальной шкале?\n"))
        notion.add_to_database(notion.change_database_data([item, choice, rating]))


if __name__ == '__main__':
    main()
