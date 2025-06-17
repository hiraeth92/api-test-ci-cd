import requests

def test_httpbin_get():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    print(f"狀態碼: {response.status_code}")
    print(f"回應內容: {response.text}")
    assert response.status_code == 200
