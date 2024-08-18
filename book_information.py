import requests

COVER_URL = 'https://covers.openlibrary.org/b/isbn/'
COVER_URL_EXTENSION = '-S.jpg'


def cover_search(isbn):
    # isbn_search = input('Enter ISBN:')
    cover_photo = COVER_URL + isbn + COVER_URL_EXTENSION
    return cover_photo


