import requests
from os import makedirs
from os.path import exists, join, basename
import os
import json
from operator import itemgetter
from dotenv import load_dotenv

load_dotenv()

SEARCH_BASE_URL = 'https://api.spotify.com/v1/search?q=/{query}&type=artist'
RELATED_BASE_URL = "https://api.spotify.com/v1/artists/{id}/related-artists"

AUTH_URL = 'https://accounts.spotify.com/api/token'


def fetch_data(url, headers):
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_related_artists(artist_id, headers):
    related_url = RELATED_BASE_URL.format(id=artist_id)
    data = fetch_data(related_url, headers)

    return data

def get_id(chart_topper, headers):
    track_info = chart_topper
    artist = track_info[1]
    artist.replace(" ", "+")

    url = SEARCH_BASE_URL.format(query=artist)

    data = fetch_data(url, headers)

    artist_id = data["artists"]["items"][0]['id']

    return artist_id

def authenticate():
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
    }

    auth_response = requests.post(AUTH_URL, data=data)
    access_token = auth_response.json().get('access_token')

    return access_token


def get_related(chart_topper):
    access_token = authenticate()
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    artist_id = get_id(chart_topper, headers)  
    related_artists = get_related_artists(artist_id, headers)

    rel_artist = related_artists["artists"][0]["name"]

    return rel_artist












