from datetime import datetime
from unittest.mock import ANY
from urllib.parse import urljoin

import pytest
import requests

TEST_BEER_ID = 42
BREWED_BEFORE_STR = '10-2015'
BREWED_BEFORE_DATE = datetime.strptime(BREWED_BEFORE_STR, '%m-%Y')
BASE_API_URL = 'https://api.punkapi.com/v2/beers/'


@pytest.fixture
def beer():
    return {'id': TEST_BEER_ID,
            'name': 'Hardcore IPA',
            'first_brewed': '12/2009',
            'image_url': 'https://images.punkapi.com/v2/42.png',
            'abv': 9.2,
            'ibu': 125,
            'target_fg': 1016,
            'target_og': 1085,
            'ebc': 40,
            'srm': 20,
            'ph': 4.4,
            'attenuation_level': 81.2,
            'contributed_by': 'Sam Mason <samjbmason>',
            'description': ANY,
            'volume': ANY,
            'boil_volume': ANY,
            'method': ANY,
            'ingredients': ANY,
            'food_pairing': ANY,
            'brewers_tips': ANY,
            'tagline': ANY
            }


def test_get_by_id_positive(beer):
    """
    Check that API returns beer by id
    """
    url = urljoin(BASE_API_URL, str(TEST_BEER_ID))
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text
    assert resp.json()[0] == beer


def test_get_filter_by_brewed_before():
    """
    Check that API can filter beer by brew date
    """
    params = f'?brewed_before={BREWED_BEFORE_STR}'
    url = urljoin(BASE_API_URL, params)
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text
    for beer in resp.json():
        first_brewed = datetime.strptime(beer['first_brewed'], '%m/%Y')
        # check that first_brewed is less than brewed_before
        assert first_brewed < BREWED_BEFORE_DATE
