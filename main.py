import requests
from bs4 import BeautifulSoup

DATA_URL = 'https://habr.com/ru/all/'
# подставлял свои значения в KEYWORDS
KEYWORDS = ['Python*']
SOURCE = requests.get(DATA_URL).text


def scrapping_habr():
    soup = BeautifulSoup(SOURCE, 'html.parser')
    for article in soup.find_all('article', class_='tm-articles-list__item'):
        headline = article.find('a', class_='tm-article-snippet__title-link').text
        preview_text = article.text
        link = article.find('a', class_='tm-article-snippet__title-link').get('href')
        date = article.find('span', class_='tm-article-snippet__datetime-published').text

        for search_word in KEYWORDS:
            if (search_word.lower() in headline.lower()) or (search_word.lower() in preview_text.lower()):
                print(f'Дата: {date} - Заголовок: {headline} - Ссылка: https://habr.com{link}')


if __name__ == '__main__':
    scrapping_habr()
