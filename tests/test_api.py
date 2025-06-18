import requests  # 匯入 requests 套件，用來進行 HTTP 請求

# 設定 API 基本網址
BASE_URL = "https://reqres.in/api"

# 預設的 request headers，這裡使用測試 API 提供的 key（實際上可省略）
HEADERS = {"x-api-key": "reqres-free-v1"}


# 測試 GET：取得第 2 頁的用戶清單
def test_get_users():
    url = f"{BASE_URL}/users?page=2"  # 目標 API 路徑
    response = requests.get(url, headers=HEADERS)  # 發送 GET 請求
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")  # 印出回應內容
    assert response.status_code == 200  # 確認 API 回傳 200 OK（成功）


# 測試 POST：新增一位使用者
def test_create_user():
    url = f"{BASE_URL}/users"  # 目標 API 路徑（建立新用戶）
    payload = {
        "name": "morpheus",     # 使用者名稱
        "job": "leader"         # 使用者職稱
    }
    response = requests.post(url, json=payload, headers=HEADERS)  # 發送 POST 請求並附上 JSON 資料
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 201  # 預期應回傳 201 Created（建立成功）


# 測試 PUT：更新使用者資訊
def test_update_user():
    url = f"{BASE_URL}/users/2"  # 更新 ID 為 2 的使用者
    payload = {
        "name": "morpheus",          # 新的名稱
        "job": "zion resident"       # 新的職稱
    }
    response = requests.put(url, json=payload, headers=HEADERS)  # 發送 PUT 請求（全量更新）
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 200  # 預期應回傳 200 OK


# 測試 DELETE：刪除一位使用者
def test_delete_user():
    url = f"{BASE_URL}/users/2"  # 刪除 ID 為 2 的使用者
    response = requests.delete(url, headers=HEADERS)  # 發送 DELETE 請求
    print(f"狀態碼: {response.status_code}, 回應內容: {response.text}")
    assert response.status_code == 204  # 預期應回傳 204 No Content（刪除成功無內容）
