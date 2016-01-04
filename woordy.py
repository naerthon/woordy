import json
import requests
import contextlib


__version__ = '0.0.2'
__author__ = "Aleph Melo"


@contextlib.contextmanager
def try_URL(message='Connection Lost'):
    try: yield
    except requests.exceptions.ConnectionError:
        print(message)


class Woordy(object):

    @staticmethod
    def __get_api_url(api):
        api_name = {
            "glosbe": "https://glosbe.com/gapi/translate?from={source_lang}&dest={dest_lang}&format=json&pretty=true&phrase={word}",
        }

        if api in api_name.keys():
            return api_name[api]
        else:
            return False


    def translate(phrase, source_lang, dest_lang):
        base_url = Woordy.__get_api_url("glosbe")
        url = base_url.format(word=phrase, source_lang=source_lang, dest_lang=dest_lang)
        req = requests.get(url).json()
        try:
            word = req['tuc'][0]['phrase']['text']

        except IndexError:
            return "Word not found. Try checking for some typo issues."

        try:
            meaning = req['tuc'][0]['meanings'][0]['text']

        except (KeyError, IndexError):
            meaning = 'Meaning not found.'

        dicty = {word: meaning}
        return dicty
