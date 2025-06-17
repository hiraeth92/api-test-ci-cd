import requests
import os

API_KEY = os.getenv("API_KEY")  # 從環境變數讀取 API key
HEADERS = {"x-api-key": API_KEY}

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201

def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url, json=payload, headers=HEADERS)
    assert response.status_code == 200

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url, headers=HEADERS)
    assert response.status_code == 204
