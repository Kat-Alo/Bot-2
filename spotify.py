from billboard import parse_chart
import requests
from os import makedirs
from os.path import exists, join, basename
import json
from operator import itemgetter

SEARCH_BASE_URL = 'https://api.spotify.com/v1/search?q=/{query}&type=artist'
RELATED_BASE_URL = "https://api.spotify.com/v1/artists/{id}/related-artists"


def fetch_data(artist, url, data_fname, dir_name):
    if exists(data_fname):
        pass
    else:
        makedirs(dir_name, exist_ok = True)
        resp = requests.get(url)
        with open(data_fname, 'wb') as f:
            f.write(resp.content)

def parse_data(artist, url):
    dir_name = artist + "_profile"
    data_fname = dir_name + "id.json"

    fetch_data(artist, url, data_fname, dir_name)
    f = open(data_fname, 'r')
    raw_data = f.read()
    f.close()
    return json.loads(raw_data)

def get_id(years_since):
    track_info = parse_chart(years_since)
    artist = track_info[1]
    artist.replace(" ", "+")

    url = SEARCH_BASE_URL.format(query=artist)
    artist_profile = parse_data(artist, url)

    artist_id = artist_profile["artists"]["items"][0]['id']

    return artist_id


def get_related(years_since):
    artist_id = get_id(years_since)

    url = RELATED_BASE_URL.format(id = artist_id)
    related_artists = parse_data(artist_id, url)

    rel_artist = related_artists["artists"][0]["name"]

    return rel_artist












