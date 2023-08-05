import csv

import requests
from bs4 import BeautifulSoup

# Создали файл с константой settung_constanta.py
import setting_constanta


def parse_content(content, index=0):
    soup = BeautifulSoup(content, 'html.parser')

    box = soup.findAll('div', class_='tp-post-card')

    # print(box)
    # print(len(box))
    # теперь мы должны распарсить какждый блок с темами

    page = []
    for block_a in box:
        block_parsing_data = {
            'Title': block_a.find('a', class_='tp-post-card__link').text,
            'Link': 'https://tproger.ru' + block_a.find('a', class_='tp-post-card__link').attrs['href'],
            'Text_info': block_a.find('p', class_='tp-post-card__text').text
        }
        # Теперь это всё необходимо сохранить в csv файл.
        # Создадим список page
        page.append(block_parsing_data)

    with open('file_csv.csv', 'w', encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file,
                                fieldnames=['Title', 'Link', 'Text_info'],
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in page:
            writer.writerow(row)

    # with open('file_csv.csv', 'r', encoding='utf-8') as r_file:
    #     print(r_file.read())


if __name__ == '__main__':

    for name in setting_constanta.pages_name:
        url = setting_constanta.base_url.format(name)
        response = requests.get(url)
        parse_content(response.content)
