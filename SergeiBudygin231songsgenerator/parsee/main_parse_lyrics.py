from typing import List
import requests
from bs4 import BeautifulSoup
import re
from parsee.parse_singers_name import get_artists_list
from tracks_text import genius_parsing_tracks_text
from utils.picklee import set_smt_list


def reformation_lyrics(data: list) -> List[List[object]]:
    lst = []
    for dt in data:
        spl_dt = re.split("\W+", dt)
        for e, i in enumerate(spl_dt):
            if i[1:] != i[1:].lower():
                big = re.search("[А-ЯA-Z][А-ЯA-Z\wa-zа-я\s]+", i[1:])
                if big is not None:
                    spl_dt[e] = i[0] + i[1:].replace(big.group(), "")
                    spl_dt.insert(e + 1, big.group())

        lst.append(spl_dt)
    return lst


def singer_tracks_text(name):
    if "/" in name:
        return None
    try:
        open(f'lyrics/{name}_tracks_text.pickle')
    except FileNotFoundError:
        link = f"https://genius.com/artists/{name}/songs"
        soup = BeautifulSoup(requests.get(link).content, features="html.parser").find_all('h3')
        lst = []
        for track in soup:
            track = track.text
            track_eng = re.search("[A-Z0-9a-z\+\-\s]+", track)
            if track_eng is not None:
                if track_eng.group() == " " or track_eng.group() == "":
                    track_eng = re.search("\([A-Z0-9a-z\+\-\s]+\)", track)
                    if track_eng is not None:
                        lst.append(genius_parsing_tracks_text(name, track_eng.group()[1:-1].replace("+", "-")))
                else:
                    lst.append(genius_parsing_tracks_text(name, track_eng.group()))
        set_smt_list(reformation_lyrics(lst), name)
    print(name, 200)


if __name__ == "__main__":
    singer_tracks_text("Basta")
    # for i in get_artists_list()[1::10]:
    #     singer_tracks_text(i)
