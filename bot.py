from billboard import parse_chart
from spotify import get_related
from datetime import date, datetime, timedelta



def bot(years_since):
    message = """{years} years ago today, {song} by {artist} was No. 1 on Billboard's Top 100. If you like this track, you might try listening to songs by {related_artist}."""


    valid_max = int(date.today().year) - 1958
    if years_since not in range(1, valid_max+1):
        return "Please enter a valid integer value."

    chart_topper = parse_chart(years_since)
    rel_artist = get_related(years_since)

    return message.format(years = str(years_since),
        song = str(chart_topper[0]),
        artist = str(chart_topper[1]),
        related_artist = str(rel_artist)
        )


