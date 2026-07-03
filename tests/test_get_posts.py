import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def test_get_existing_post():
    response = requests.get(f"{BASE_URL}/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data
    assert data["title"] != ""
    assert data["body"] != ""


def test_get_non_existing_post():
    response = requests.get(f"{BASE_URL}/999999")

    assert response.status_code == 404

    data = response.json()

    assert data == {}

def test_get_all_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    post1 = data[1]
    assert post1["title"] == 'qui est esse'
    assert 'userId' in post1
