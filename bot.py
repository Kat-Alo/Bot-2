from billboard import parse_chart
from spotify import get_related
from datetime import date, datetime, timedelta

import sys



def bot(years_since):
    message = """{years} years ago today, {song} by {artist} was No. 1 on Billboard's Top 100. If you like this track, you might try listening to songs by {related_artist}."""


    valid_max = int(date.today().year) - 1958
    if years_since not in range(1, valid_max+1):
        return "Please enter a valid integer value."

    chart_topper = parse_chart(years_since)
    rel_artist = get_related(chart_topper)

    print (message.format(years = str(years_since),
        song = str(chart_topper[0]),
        artist = str(chart_topper[1]),
        related_artist = str(rel_artist)
    ))


if __name__ == '__main__':

    years_since = 10
    if len(sys.argv) > 1:
        years_since = int(sys.argv[1])

    bot(years_since)


