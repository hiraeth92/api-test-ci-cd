import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres-free-v1"}

def test_get_users():
    url = f"{BASE_URL}/users?page=2"
    response = requests.get(url, headers=HEADERS)
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 200

def test_create_user():
    url = f"{BASE_URL}/users"
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(url, json=payload, headers=HEADERS)
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 201

def test_update_user():
    url = f"{BASE_URL}/users/2"
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url, json=payload, headers=HEADERS)
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 200

def test_delete_user():
    url = f"{BASE_URL}/users/2"
    response = requests.delete(url, headers=HEADERS)
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 204
