import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_create_user():
    url = "https://reqres.in/api/users"
    headers = {"x-api-key": "reqres-free-v1"}
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201

def test_update_user():
    url = "https://reqres.in/api/users/2"
    headers = {"x-api-key": "reqres-free-v1"}
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    headers = {"x-api-key": "reqres-free-v1"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
