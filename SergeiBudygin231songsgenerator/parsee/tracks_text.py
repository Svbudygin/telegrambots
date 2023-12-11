import requests
from bs4 import BeautifulSoup


def genius_parsing_tracks_text(singer, track):
    link = f'https://genius.com/{singer.replace(" ", "-")}-{track.replace(" ", "-")}-lyrics'
    soup = BeautifulSoup(requests.get(link).content, "html.parser")
    track_text = soup.find_all("div", {"class": "Lyrics__Container-sc-1ynbvzw-1"})
    return "\n".join([span.text.strip() + " " for span in track_text])


if __name__ == "__main__":
    pass
