import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_create_post_with_valid_data():
    post_data = { "title": "QA Portfolio", "body": "API Testing", "userId": 1 }
    response = requests.post(BASE_URL, json=post_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == post_data["title"]
    assert data["body"] == post_data["body"]
    assert data["userId"] == post_data["userId"]
    
def test_create_post_without_title():
    post_data = { "body": "API Testing", "userId": 1 }
    response = requests.post(BASE_URL, json=post_data)
    assert response.status_code == 201
    data = response.json()
    assert "title" not in data
    assert "id" in data
    assert data["body"] == post_data["body"]
    assert data["userId"] == post_data["userId"]

def test_create_post_with_empty_title():
    post_data = { "title": "", "body": "API Testing", "userId": 1 }
    response = requests.post(BASE_URL, json=post_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == post_data["title"]
    assert data["body"] == post_data["body"]
    assert data["userId"] == post_data["userId"]