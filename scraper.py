import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re
import lxml


def get_raw_html(url: str):
    '''
    Return raw html from a given url.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()

        response.encoding = 'utf-8'
        raw_html = response.text
    except HTTPError as http_err:
        print(f'HTTP error has occured: {http_err}')

    return raw_html


def get_acting_credits_count(url: str):
    '''
    Parse Katie's imdb page & return the number of acting credits.
    '''
    try:
        html = get_raw_html(url)
        soup = BeautifulSoup(html, 'lxml').find(
            'div', {'id': 'filmo-head-actress'})

        # Should return number of credits string.
        credits_string = (re.search('\d+ credits', str(soup))).group()

        # Gets the number part and turns to an int.
        number = int(credits_string.split(' ')[0])

        return number

    except HTTPError as http_err:
        print(f'HTTP error has occured: {http_err}')
