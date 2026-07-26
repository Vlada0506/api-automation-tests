import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_delete_existing_post():
    response = requests.delete(f'{BASE_URL}/1')
    assert response.status_code == 200
    data = response.json()
    assert data == {}

def test_delete_non_existing_post():
    response = requests.delete(f'{BASE_URL}/99999')
    assert response.status_code == 200
    data = response.json()
    assert data == {}