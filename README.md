# Woordy
A backend service from an MVP on its way. 

## Installation
```
$ git clone git@github.com:alephmelo/woordy.git
$ cd woordy
```

## Usage
Gets the translations for a given word, calls the glosbe API for getting the translation.

`source_lang>` and `<dest_lang>` languages should be specifed in 3-letter ISO 639-3 format, although many 2-letter codes (en, de, fr) will work. 

See http://en.wikipedia.org/wiki/List_of_ISO_639-3_codes for full list.

``` python
>>> from woordy import Woordy
>>> Woordy.translate('book', 'en', 'de')
['Buch', {'meaning': 'collection of sheets of paper bound together containing printed or written material'}]
```
