import requests
import json


URL = 'http://127.0.0.1:5000'


def test_get_default_card():
    response = requests.get(URL + '/api/cards/0')
    assert response.status_code == 200
    assert response.json()['title'] == 'Default'
    assert response.json()['content'] == ["Some Text1", "Some Text2"]


def test_get_nonexistent_card():
    response = requests.get(URL + '/api/cards/9999')
    assert response.status_code == 404
    assert response.json()['message'] == 'Card with id=9999 was not found!'


def test_get_invalid_id():
    response = requests.get(URL + '/api/cards/invalid_id')
    assert response.status_code == 404
    assert response.json()['message'] == 'Card with id=invalid_id was not found!'
