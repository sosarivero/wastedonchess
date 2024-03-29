import re
import requests
import sys
from datetime import datetime, timedelta


def main():
    player = input("Chess.com username: ")
    year = input("Year (yyyy): ")
    month = input("Month (mm): ")

    games_archive = get_chesscom_archive(player, year, month)

    result = get_total_length(games_archive)
    gamelength = result[0]
    games = result[1]

    print(
        f"{player} has played {games} games for a total time of {gamelength} during {year}/{month}"
    )


def get_chesscom_archive(player: str, year: str, month: str):
    """
    Takes a username, a year (four digits) and a month (zero-padded).
    Returns a json of the queried user's Chess.com games during said month.
    """
    archive = requests.get(
        f"https://api.chess.com/pub/player/{player}/games/{year}/{month}"
    )

    archive = archive.json()

    try:
        if "games" in archive:
            return archive
        elif "code" in archive:
            raise ValueError
    except ValueError:
        sys.exit(f"ERROR: {archive['code']}")


def get_pgn_gamelength(pgn: str):
    """
    Take a Chess game in pgn format, extracts the start and end times, and
    returns the difference (i.e the total game's length) as a timedelta object.
    """
    pgn_start = re.search(r"(?:StartTime \")(\d{2}[:]\d{2}[:]\d{2})", pgn).group(1)
    pgn_end = re.search(r"(?:EndTime \")(\d{2}[:]\d{2}[:]\d{2})", pgn).group(1)

    start_time = datetime.strptime(pgn_start, "%H:%M:%S")
    end_time = datetime.strptime(pgn_end, "%H:%M:%S")

    gamelength = end_time - start_time

    return gamelength.total_seconds()


def get_total_length(archive: dict):
    """
    Takes an archive of games generated by get_chesscom_archive().
    Returns a tuple that contains the total length of all the games contained
    within the archive, and the total number of games played.
    """
    total_time = 0

    games_qty = len(archive["games"])

    for game in archive["games"]:
        pgn = game["pgn"]
        total_time += get_pgn_gamelength(pgn)

    timedelta_total = str(timedelta(seconds=total_time))

    return timedelta_total, games_qty


if __name__ == "__main__":
    main()
