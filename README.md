# Bot-2

The bot returns to the user that song that was No. 1 on Billboard's Top 100 on the current day, a given number of years ago. The message includes the song title, artist and one suggested artist.

How to use this:

import bot
bot.bot(10)

output:
"10 years ago today, This Is Why I'm Hot by Mims was No. 1 on Billboard's Top 100. If you like this track, you might try listening to songs by Jibbs."

I used data from Billboard's Top 100 Charts site and the Spotify API.

The bot generates a URL based on the current date and number of years entered by the user. It then finds a valid page by requesting a Billboard Top 100 Chart URL and modifying the date to one day prior until it can find the chart that had been most recently updated on the requested date. 

Once the bot parses the correct chart and identifies the top song and artist, the spotify.py file identifies a related artist. First, this file locates the artist ID, as required by the Spotify related artists request parameter. Then, the file generates the URL to retrieve the related artists json file and returns the first listed related artist.

The bot does not handle situations in which the artist for a track does not have their own profile on Spotify. For instance, 5 years ago, the top track was Some Nights by 'fun. Featuring Janelle Monae.' Both fun. and Janelle Monae have their own profiles, but there is not an artist object for them together. The code would not sort the proper query from the returned string and the code would throw an error.
