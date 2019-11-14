import requests
import json


URL = 'http://127.0.0.1:5000'


def test_list_cards():
    response = requests.get(URL + '/api/pools')
    assert response.status_code == 200
    for card in response.json()['items']:
        assert card.get('id', None) is not None
        assert card.get('title', None) is not None
