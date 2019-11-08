import requests
from bs4 import BeautifulSoup


class CinemaParser():
    def __init__(self, city='msk'):
        self.city = city
        if self.city == 'msk':
            self.url = 'https://msk.subscity.ru'
        else:
            self.url = 'https://spb.subscity.ru'
        self.content = None

    def extract_raw_content(self):
        content = requests.get(self.url)
        self.content = content.text
        return self.content

    def print_raw_content(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        print(soup.prettify())

spb_parser = CinemaParser()
spb_parser.extract_raw_content()
spb_parser.print_raw_content()


