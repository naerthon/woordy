import json
import requests
import contextlib


__version__ = '0.0.1'
__author__ = "Aleph Melo"


@contextlib.contextmanager
def try_URL(message='Connection Lost'):
    try: yield
    except requests.exceptions.ConnectionError:
        print(message)


class Woordy(object):

    @staticmethod
    def __get_api_link(api):
        api_name2links = {
            "glosbe": "https://glosbe.com/gapi/translate?from={source_lang}&dest={dest_lang}&format=json&pretty=true&phrase={word}",
        }

        if api in api_name2links.keys():
            return api_name2links[api]
        else:
            return False


    def translate(phrase, source_lang, dest_lang):
        base_url = Woordy.__get_api_link("glosbe")
        url = base_url.format(word=phrase, source_lang=source_lang, dest_lang=dest_lang)
        req = requests.get(url).json()
        word = req['tuc'][0]['phrase']['text']
        meaning = req['tuc'][0]['meanings'][0]['text']
        dicty = {word : meaning}
        return dicty
