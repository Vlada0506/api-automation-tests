import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_update_existing_post():
    updated_data = { "title": "API Testing", "body": "PUT", "userId": 1 }
    response = requests.put(f'{BASE_URL}/1', json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == updated_data["title"]
    assert data["body"] == updated_data["body"]
    assert data["userId"] == updated_data["userId"]

def test_update_non_existing_post():
    updated_data = { "title": "API Testing", "body": "PUT", "userId": 1 }
    response = requests.put(f'{BASE_URL}/99999', json=updated_data)
    assert response.status_code == 500
    assert "Cannot read properties of undefined" in response.text