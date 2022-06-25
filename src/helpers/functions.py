"""
Basic functions to manipulate data, etc
"""

def get_key(searched_key: str, data: dict) -> dict:
    """
    Gets specific key from dictionary, even if 
    it is a key nested in other dictionaries.
    """
    response = {}
    if isinstance(data, dict):
        if searched_key in data.keys():
            return data[searched_key]
        else:
            for k, v in data.items():
                response.update(get_key(searched_key, v))
    return response
