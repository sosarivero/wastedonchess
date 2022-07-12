import re
import requests

player = requests.get("https://api.chess.com/pub/player/hikaru/games/archives").json()


games = requests.get("https://api.chess.com/pub/player/hikaru/games/2022/07").text

starts = re.findall(r"(?:StartTime \\\")(\d{2}[:]\d{2}[:]\d{2})", games)
ends = re.findall(r"(?:EndTime \\\")(\d{2}[:]\d{2}[:]\d{2})", games)

start_times = starts
end_times = ends

print(end_times)
print(len(end_times))
# StartTime regex: r"(?:StartTime \\\")(\d{2}[:]\d{2}[:]\d{2})"
# EndTime regex: r"(?:EndTime \\\")(\d{2}[:]\d{2}[:]\d{2})"
