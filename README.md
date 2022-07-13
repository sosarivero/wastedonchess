# Wasted on Chess

#### Video Demo: https://www.youtube.com/watch?v=AcxWbzsEKxE

## Overview

### Summary

A simple application that connects with Chess.com's Published API, and with a given username, year and month returns the total amount of games and the total game length of the chess games played in Chess.com by that user in the given month.

Inspired by the website WastedonLoL, which shows the amount of real-life time that players have "wasted" on the online videogame League of Legends. A lot of online gaming platforms show total game time as a statistic to its users, and I thought Chess platforms are missing this, specially for a game that revolves so much around time management.

As it stands right now, as a CLI application, it does not really offer any usability that could be desired by any user. My intention is to use this as the basis for a web application, that would recreate user statistics websites that are so common for online competitive videogames, but in the context of online chess and its most popular platforms. It is very possible that I would submit such website as the final Django project for the CS50w course.

### Python skills demonstrated within this project

-   Use of time libraries.
-   Use of HTTP requests.
-   Testing with PyTest.
-   Use of regex.

### Dependencies

The only non-standard library used in the project is requests, which is nevertheless available by default in the CS50 codespace and also in most Linux distributions, so I am not sure of how necessary is it to include in the requeriments.txt file.

I started the project by using urllib as provided in the standard libraries, but quickly switched to just use requests as it seems to be hauled by the Python community as the best solution for HTTP requests, and is not included as a standard because of some politics or maintenance technicalities.

In the future I would like to also connect with Lichess API, the other major online Chess platform, but it uses a 3rd party Python API and I did not want to boggle down or over-complicate the project submission by using it.

### Chess.com API

I made use of the Published-Data API provided by Chess.com, which is documented in [this link](https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive).

The application mainly uses of the Player Games (aka 'archives') and the game objects contained within them.

Chess.com saves user games within monthly archives.

The initial intention of this application was to sum up the total amount of games in the lifetime of a player's account, and sum up their lengths and maybe even categorize by time control and so on, but this proved to not be viable as many users have played upwards of ten thousand games across almost a decade, and the throttling of the API made the output of the application **incredibly** slow. I am not sure if this could be optimized well enough within Python.

### Inner workings

As mentioned before, each user has monthly archives of their games. Each monthly archive contains "game objects", which include a myriad of information about the played game, such as the users that took part in it, their colors, the time control, etc. What is of interest to us is the timestamps of when the game started and when it finished.

This information is contained within the game's PGN. Portable Game Notation (PGN) is a standard plain text format for recording chess games (both the moves and related data), which can be read by humans and is also supported by most chess software.

Chess.com's PGN includes the tags StartTime and EndTime. The PGN is a really long string. The method used to get this information is by using regex and re.search():

`r"(?:StartTime \")(\d{2}[:]\d{2}[:]\d{2})"`

`r"(?:EndTime \")(\d{2}[:]\d{2}[:]\d{2})"`

By using this regex and the capture group, we can then make use of the datetime module (more specifically, the timedelta object) in order to get the difference between the times (i.e the length of the match). This is returned as the total amount of seconds, in order to be used by the final function that sums up every game included within an archive, and returns a tuple of (total games, total gamelength).

#### Current issues

There is an issue when handling total game lengths that span multiple days. This is not an issue for most online chess players, as the most popular time controls are really short, but it can be a problem for those that practice classical formats online. This problem is clearly a by-product of the timedelta object. I decided to submit the project before finishing this because CS50P's final project was a source of anxiety for me, and I wanted to submit it as soon as possible.

I will make sure to make this application's functionality more pristine for when I submit it as a Django back-end for CS50w.

### Thanks

Thanks to CS50, Harvard university, David Malan's and its team for making this incredible educational resource available for free.

Thanks to all the moderators in the Discord and Reddit communities. Thanks to their hard work CS50 is a joy of an online community to participate within.

Thanks to StackOverflow, RegExr and well-documented libraries.
