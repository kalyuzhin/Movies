import os
import sys

with open('config.txt', 'r') as file:
    FILEPATH = file.readlines()[-1]


def add_movie(options: list) -> None:
    if options[1] == '1':
        status = 'Want to watch'
    else:
        status = 'Watched'

    if options[-1] == 1:
        item_type = 'Movie'
    elif options[-1] == 2:
        item_type = 'Series'
    elif options[-1] == 3:
        item_type = 'Cartoon'
    elif options[-1] == 4:
        item_type = 'Anime'
    else:
        return

    rating = '⭐️' * options[2]
    name = options[0][0][:-5:]
    year = int(options[0][0][-4::])
    link = options[0][1]

    with open(FILEPATH, 'r') as file:
        content = file.read()

    if (content.find(f'<tr>\n<td>{name}</td><td>{year}</td>')):
        print('Already added to your table')
        return

    with open(FILEPATH, 'w') as file:
        file.write(content[
                   :-18] + f'<tr>\n<td>{name}</td>'
                           f'<td>{year}</td>'
                           f'<td>{item_type}</td>'
                           f'<td>{status}</td>'
                           f'<td>{rating}</td>'
                           f'<td><a href=\'{link}\'>Link</a></td>'
                           f'</tr>\n</tbody>\n</table>\n')


def add_from_csv(line: str) -> None:
    options = line.split(',')
    with open(FILEPATH, 'r') as file:
        content = file.read()

    with open(FILEPATH, 'w') as file:
        file.write(content[
                   :-18] + f'<tr>\n<td>{options[0]}</td>'
                           f'<td>{options[1]}</td>'
                           f'<td>{options[2]}</td>'
                           f'<td>{options[3]}</td>'
                           f'<td>{options[4]}</td>'
                           f'<td><a href=\'{options[5]}\'>Link</a></td>'
                           f'</tr>\n</tbody>\n</table>\n')
