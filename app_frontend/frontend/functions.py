import re
import unicodedata
from urllib.parse import urljoin

def has_diacritics_or_punctuation(input_string):
  # Use regex to find diacritics or punctuated letters
  pattern = r'[^\w\s]'
  pattern_match = re.search(pattern, unicodedata.normalize('NFKD', input_string))
  return bool(pattern_match)

# Constants for regex patterns and characters
COMMA_PATTERN = r'^(.*?),\s*(.*?)$'
DIACRITICS_PUNCTUATION_PATTERN = r'[^\w\s]'
SPACE_PATTERN = r'[^a-zA-Z0-9]+'
UNDERSCORE = '_'
SPACE = ' '

def preprocess_string(string):
    # Check for comma and process accordingly
    if ',' in string:
        rearranged_string = re.sub(COMMA_PATTERN, r'\2 \1', string).lower().replace(SPACE, UNDERSCORE).rstrip()
        if has_diacritics_or_punctuation(rearranged_string):
            rearranged_string = re.sub(DIACRITICS_PUNCTUATION_PATTERN, '', unicodedata.normalize('NFKD', rearranged_string)).lower().replace(SPACE, UNDERSCORE).rstrip(UNDERSCORE)
    # Check for diacritics or punctuation and process accordingly
    elif has_diacritics_or_punctuation(string):
        if '-' in string:
            rearranged_string = re.sub(r'[-]', UNDERSCORE, unicodedata.normalize('NFKD', string)).lower().replace(SPACE, UNDERSCORE).rstrip(UNDERSCORE)
            if has_diacritics_or_punctuation(rearranged_string):
                rearranged_string = re.sub(DIACRITICS_PUNCTUATION_PATTERN, '', unicodedata.normalize('NFKD', rearranged_string)).lower().replace(SPACE, UNDERSCORE).rstrip(UNDERSCORE)
        else:
            rearranged_string = re.sub(DIACRITICS_PUNCTUATION_PATTERN, '', unicodedata.normalize('NFKD', string)).lower().replace(SPACE, UNDERSCORE).rstrip(UNDERSCORE)
    # Process as a regular column name
    else:
        transformed_string = re.sub(SPACE_PATTERN, UNDERSCORE, string).lower()
        rearranged_string = transformed_string.rstrip(UNDERSCORE)

    return unicodedata.normalize('NFKD', rearranged_string).encode('ASCII', 'ignore').decode('utf-8')



def endpoint_decorator(base_url, endpoint_path):
    def decorator(function):
        def wrapper(*args, **kwargs):
            # Construct the full endpoint URL by appending the endpoint path to the base URL
            endpoint = f"{base_url}{endpoint_path}"
            return function(endpoint, *args, **kwargs)
        return wrapper
    return decorator