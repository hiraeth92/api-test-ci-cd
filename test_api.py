import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200
    assert "data" in response.json()
