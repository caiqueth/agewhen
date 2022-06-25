import requests
from datetime import datetime
from config.settings import Settings

OMDB_URL = Settings.omdb_url()

def get_movie_release_date(movie_title: str) -> datetime.date:
    response = requests.get(OMDB_URL + f"&t={movie_title}")

    if response.status_code != 200:
        if response.status_code == 401:
            raise Exception("Could not access the OMDB API! Status was 401, maybe check if your API Key is valid?")
        else:
            raise Exception("Could not access the OMDB API! Response {}".format(response.status_code))

    info = response.json()
    date = info.get("Released", None)

    if date is None:
        raise Exception("Could not find the release date for that movie :(")

    date = datetime.strptime(date, "%d %b %Y")

    return date.date()
