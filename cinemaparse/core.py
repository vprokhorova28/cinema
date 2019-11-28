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
        x, films = [], []
        div_tags = self.soup.find_all('div', {'class': 'movie-plate-row'})
        for i in div_tags[::2]:
            x.append(i.find_all('a', {'class': 'underdashed'}))
        for i in x:
            films.append(i[0].text)
            return films

    def get_film_nearest_session(self, name):
        if not self.content:
            self.extract_raw_content()
        x, date = [], []
        div_tags = self.soup.find_all('div', {'class': 'movie-plate-row'})
        for i in div_tags[::2]:
            x.append(i.find_all('a', {'class': 'underdashed'}))
        for i in div_tags[1::2]:
            for j in (i.find_all('div', {'class', 'movie-next-screening-mobile'})):
                for k in (j.find_all('span', {'class': 'label label-bg label-default normal-font'})):
                    date.append(k.text)
        f = zip(x, date)
        for i in f:
            if i[0][0].text == name:
                if 'сегодня' in i[1]:
                    url = self.url + i[0][0]['href']
                else:
                    return (None, None)
        content1 = requests.get(url)
        content1 = content1.text
        content1 = BeautifulSoup(content1, 'html.parser')
        minn = 100000000000000000
        y = []
        new_div_tags = content1.find_all('table', {'class': 'table table-bordered table-condensed table-curved table-striped table-no-inside-borders'})
        name_part = new_div_tags[0].find_all('td', {'class': 'col-sm-4 col-xs-11'})
        time_part = new_div_tags[0].find_all('td', {'class': 'col-sm-8 col-xs-1'})
        times = []
        names = []
        for i in time_part:
            times.append(i.find_all('td', {'class': 'text-center cell-screenings'}))
        for i in name_part:
           names.append(i.find_all('div', {'class': 'cinema-name'}))
        inf = zip(times, names)
        for i in names:
            y.append(i[0].text)
        inf = zip(times, y)
        for i in inf:
            if int(i[0][0]['attr-time']) < minn:
                minn = int(i[0][0]['attr-time'])
                time = i[0][0].text[:5]
                name = i[1]
        return (name, time)
