from datetime import datetime

import requests
from config.settings import Settings
from helpers.functions import get_key


def get_person_birthday(person_name: str) -> datetime.date:
    wikipedia_info_url = Settings.WIKIPEDIA_INFO_URL
    wikidata_person_info_url = Settings.WIKIDATA_PERSON_INFO_URL

    response = requests.get(wikipedia_info_url.format(person_name))
    if response.status_code != 200:
        raise Exception("Could not access Wikipedia")

    info = response.json()

    prop_id = get_key("pageprops", info).get('wikibase_item', None)

    if prop_id is None:
        raise Exception("Could not find a person with that name in Wikipedia")

    person_info_response = requests.get(wikidata_person_info_url.format(prop_id))
    if person_info_response.status_code != 200:
        raise Exception("Could not access WikiData")

    person_info = person_info_response.json()
    if 'error' in person_info.keys():
        raise Exception("Could not find that person in Wikidata")

    try:
        # damn that's some huge nesting
        raw_birthday = person_info['entities'][prop_id]['claims']['P569'][0]['mainsnak']['datavalue']['value']['time']
    except KeyError:
        raise Exception("The person has been found, but there is no birthday information")

    birthday = datetime.strptime(raw_birthday, '+%Y-%m-%dT%H:%M:%SZ')

    return birthday.date()
