from parsers import *
from notion import *
from obsidian import *


def main() -> None:
    while True:
        item_type = int(input('Введите тип:\nФильм - 1\nСериал - 2\nМультфильм - 3\nАниме - 4\n\nВыход - 0\n'))
        if not item_type:
            exit(0)
        name = input("Введите название фильма или сериала:\n")
        service = input("Введите, где хотите найти его(кинопоиск или IMDB)\n1 - кинопоиск\n2 - IMDB\n")
        if service.strip().lower() == '1':
            items = kinopoisk_functions.parse_kinopoisk_page(kinopoisk_functions.create_kinopoisk_url(name))
        elif service.strip().lower() == '2':
            items = imdb_functions.parse_imdb_page(imdb_functions.create_imdb_url(name))
        else:
            print('Ошибка!')
            return
        i = 1
        for elem in items:
            print(f'\t{i}.{elem} - {items[elem]}')
            i += 1
        print("Выберите нужный вам элемент(скопируйте и вставьте его название):")
        name = input()
        item = next((k, v) for k, v in items.items() if k == name)
        print("Вы хотите его посмотреть или вы уже его просмотрели?\n1 - хочу посмотреть\n2 - просмотрен")
        choice = input().strip().lower()
        if choice == '1':
            # notion.want_to_watch(notion.change_data(result, name))
            # notion.add_to_database(notion.change_database_data([item, choice, 0, item_type]))
            obsidian.add_movie([item, choice, 0, item_type])
        elif choice == '2':
            # notion.already_watched(notion.change_data(result, name))
            rating = int(input("Как вы оцените этот фильм по десятибальной шкале?\n"))
            # notion.add_to_database(notion.change_database_data([item, choice, rating, item_type]))
            obsidian.add_movie([item, choice, rating, item_type])


def add_from_file(file_name: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            add_from_csv(line)
            print(line)


if __name__ == '__main__':
    main()
    # add_from_file('Movies 25f051b0d0174c4593f593809a34fc97.csv')
