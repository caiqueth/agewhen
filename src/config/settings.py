from decouple import config


class Settings:
    OMDB_KEY = config('OMDB_KEY', cast=str)
    OMDB_ROOT = config('OMDB_URL', cast=str)
    WIKIPEDIA_INFO_URL = config('WIKIPEDIA_INFO_URL', cast=str)
    WIKIDATA_PERSON_INFO_URL = config('WIKIDATA_PERSON_INFO_URL', cast=str)

    @classmethod
    def omdb_url(cls):
        return cls.OMDB_ROOT + "?apikey=" + cls.OMDB_KEY
