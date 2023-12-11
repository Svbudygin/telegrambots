import pickle
import requests
from bs4 import BeautifulSoup

""" разово запарсил список рускоязычных исполнитей с genius"""

def set_artists_list():
    try:
        open('../artist_list_of_names.pickle')
    except FileNotFoundError:
        url = f"https://genius.com/discussions/265505-Genius"
        response = requests.get(url).content
        soup = BeautifulSoup(response, features="html.parser")
        soup = soup.find_all('a', {"rel": "noopener"})
        with open('../artist_list_of_names.pickle', 'wb') as f:
            return pickle.dump(list(map(lambda x: x.text, soup)), f, pickle.HIGHEST_PROTOCOL)


def get_artists_list():
    with open('../artist_list_of_names.pickle', 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    set_artists_list()
    print(get_artists_list())
