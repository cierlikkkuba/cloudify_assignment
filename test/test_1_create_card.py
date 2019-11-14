import requests
import json


URL = 'http://127.0.0.1:5000'
HEADERS = {'Content-Type': "application/json"}


def test_create_default_card():
    payload = {
        "title": "test_card",
        "content": ["Some Text1",
                    "Some Text2"]
    }
    response = requests.put(URL + '/api/cards/1', data=json.dumps(payload), headers=HEADERS)
    assert response.status_code == 201
    assert response.json()['title'] == 'test_card'
    assert response.json()['content'] == ["Some Text1", "Some Text2"]


def test_create_card_1337():
    payload = {
        "title": "test_card_1337",
        "content": ["Some Text1 1337",
                    "Some Text2 1337"]
    }
    response = requests.put(URL + '/api/cards/1337', data=json.dumps(payload), headers=HEADERS)
    assert response.status_code == 201
    assert response.json()['title'] == 'test_card_1337'
    assert response.json()['content'] == ["Some Text1 1337", "Some Text2 1337"]


def test_create_card_loop():
    for i in range(1, 10, 2):
        payload = {
            "title": f"test_card_{i}",
            "content": [f"Some Text1 {i}",
                        f"Some Text2 {i}"]
        }
        response = requests.put(URL + f'/api/cards/{i}', data=json.dumps(payload), headers=HEADERS)
        assert response.status_code == 201
        assert response.json()['title'] == f'test_card_{i}'
        assert response.json()['content'] == [f"Some Text1 {i}", f"Some Text2 {i}"]
