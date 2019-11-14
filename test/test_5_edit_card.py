import requests
import json


URL = 'http://127.0.0.1:5000'
HEADERS = {'Content-Type': "application/json"}


def test_edit_one_card():
    card_id = 1
    payload = {
        "title": "updated_test_card",
        "content": ["Another Text1",
                    "Another Text2"]
    }
    response = requests.put(URL + f'/api/cards/{card_id}/edit', data=json.dumps(payload), headers=HEADERS)
    assert response.status_code == 201
    assert response.json()['title'] == "updated_test_card"
    assert response.json()['content'] == ["Another Text1", "Another Text2"]


def test_edit_nonexistent_card():
    card_id = 99999
    payload = {
        "title": "updated_test_card",
        "content": ["Another Text1",
                    "Another Text2"]
    }
    response = requests.put(URL + f'/api/cards/{card_id}/edit', data=json.dumps(payload), headers=HEADERS)
    assert response.status_code == 404
    assert response.json()['message'] == f'Card with id={card_id} was not found!'
