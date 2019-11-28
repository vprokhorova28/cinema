from cinemaparse import CinemaParser

spb_parser = CinemaParser('spb')
spb_parser.extract_raw_content()
spb_parser.print_raw_content()
print(spb_parser.get_films_list())
print(spb_parser.get_film_nearest_session('Джокер'))
