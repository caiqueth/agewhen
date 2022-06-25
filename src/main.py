import sys

from apis.omdb import get_movie_release_date
from apis.wikidata import get_person_birthday

from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    person_name, movie_title = sys.argv[1], sys.argv[2]
    person_birthday = get_person_birthday(person_name)
    movie_release_date = get_movie_release_date(movie_title)
    person_age = relativedelta(movie_release_date, person_birthday).years

    response = f"""
        {person_name} was born in {person_birthday} and {movie_title} released in {movie_release_date}
        By that time, {person_name} was {person_age} years old.
    """

    print(response)
