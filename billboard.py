from datetime import date, datetime, timedelta
import requests
from bs4 import BeautifulSoup
import urllib

BASE_URL = 'http://www.billboard.com/charts/hot-100/'

#find the search date, given the current days and years since the song topped charts
def get_date(years_since):
    today = date.today()
    new_year = today.year - years_since
    new_date = today.replace(year = new_year)

    return new_date.strftime("%Y-%m-%d")

#returns the date prior as a string
def get_yesterday(this_date):
    datetime_object = datetime.strptime(this_date, '%Y-%m-%d')
    yesterday = datetime_object - timedelta(1)

    return yesterday.strftime('%Y-%m-%d')

#gets url of chart for that date; if there were no changes in the chart, the chart for the most
#recent date applies (e.g. if No. 1 change last Tuesday, but hasn't changed since, the same
#track would be at No. 1 today)
def get_url(years_since):
    date = get_date(years_since)
    url = BASE_URL + date
    resp = requests.get(url)

    while resp.status_code == 404:
        date = get_yesterday(date)
        url = BASE_URL + date
        resp = requests.get(url)

    return url

#returns the top track and artist name for given day
def parse_chart(years_since):
    url = get_url(years_since)
    f = urllib.request.urlopen(url)
    html = f.read()
    html.decode("utf-8")
    soup = BeautifulSoup(html, 'lxml')
    f.close()

    track_info = []

    song = soup.find("a", {"class": "c-title__link lrv-a-unstyle-link"}).get_text(strip=True)
    artist = soup.select("p.c-tagline.a-font-primary-l")[0].text.strip()

    track_info.append(song)
    track_info.append(artist)

    return track_info
















