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
        self.soup = BeautifulSoup(self.content, 'html.parser')
        return self.content

    def print_raw_content(self):
        print(self.soup.prettify())
    
    def get_films_list(self):
        if not self.content:
            self.extract_raw_content()
        x = []
        div_tags = self.soup.find_all('div', {'class': 'movie-plate-row'})
        for i in div_tags[::2]:
            x.append(i.find_all('a', {'class': 'underdashed'}))
        for i in x:
            print(i[0].text)

    def get_film_nearest_session(self, name):
        if not self.content:
            self.extract_raw_content()
        x = []
        div_tags = self.soup.find_all('div', {'class': 'movie-plate-row'})
        for i in div_tags[::2]:
            x.append(i.find_all('a', {'class': 'underdashed'}))
        for i in x:
            if i[0].text == name:
                url = self.url + i[0]['href']
        content1 = requests.get(url)
        content1 = content1.text
        content1 = BeautifulSoup(content1, 'html.parser')
        minn = 100000000000000000
        new_div_tags = content1.find_all('table', {'class': 'table table-bordered table-condensed table-curved table-striped table-no-inside-borders'})
        for i in new_div_tags:
             y = i.find_all('td', {'class': 'text-center cell-screenings'})
             z = i.find_all('a', {'class': 'underdashed'})
             t = i.find_all('a', {'class': 'btn btn-default navbar-btn price-button cell-screening-desktop'})
        for i, j in y, z:
            '''a = i['attr-time']'''
            print(i)
            '''if int(a) < minn:
                minn = int(a)
                name = j.text
                time = i.text
        return (name, time)'''
