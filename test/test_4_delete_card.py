import requests
import json


URL = 'http://127.0.0.1:5000'


def test_delete_one_card():
    card_id = 3
    response = requests.delete(URL + f'/api/pools/{card_id}')
    assert response.status_code == 204
    list_response = requests.get(URL + '/api/pools')
    for card in list_response.json()['items']:
        assert card.get('id', None) is not f'{card_id}'
