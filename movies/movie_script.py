from bs4 import BeautifulSoup
import requests


def get_movies(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    movies = soup.find('tbody', {'class': 'lister-list'})
    movies_list = []
    
    for movie in movies.findAll('tr'):
        try:
            movies_dict = dict()
            movies_dict["rating"] = movie.find('td', {'class': 'ratingColumn'}).find('strong').text
            movies_dict["title"] = movie.find('td', {'class': 'titleColumn'}).find('a').text
            movie_url = movie.find('a').get('href')
            movies_dict["imdb_key"] = movie_url.split('/')[2]
            movie_url = 'https://www.imdb.com'+movie_url
            movie_soup = BeautifulSoup(requests.get(movie_url).text, "html.parser")
            movie_details = movie_soup.find('div', {'class': 'subtext'}).text.split('|')
            movies_dict["type_rating"] = movie_details[0].replace('\n', '').strip()
            movies_dict["duration"] = movie_details[1].replace('\n', '').strip()
            movies_dict["genre"] = movie_details[2].replace('\n', '').strip()
            movies_dict["release_date"] = movie_details[3].replace('\n', '').strip()
            movies_list.append(movies_dict)
        except Exception as e:
            print(str(e))
            continue
        
        
    return movies_list
