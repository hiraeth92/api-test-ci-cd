# 🚀 Automated RESTful API Testing with CI/CD

[![Test Coverage Report](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://hiraeth92.github.io/api-test-ci-cd/)
![Coverage](https://img.shields.io/badge/Coverage-Auto--Generated-brightgreen?style=flat-square&logo=codecov)
---

## 📌 專案簡介

本專案專注於構建一套自動化測試與持續整合／持續部署（CI/CD）流程，藉由 **Python + Pytest + GitHub Actions** 技術，針對 RESTful API 提供涵蓋多種 HTTP 方法的完整測試架構，並結合報告自動產出與可視化成果發佈。設計上強調模組化、可擴充性與實務導向，模擬實際團隊維運環境的需求與品質控管流程。

核心功能包括：
- 撰寫高可讀性的自動化測試腳本（涵蓋 GET / POST / PUT / DELETE）
- 整合 pytest-cov 產生 HTML 覆蓋率報告
- 透過 GitHub Actions 自動執行測試與部署流程
- 成果以 GitHub Pages 公開報告，實現測試透明化與品質追蹤

---

## 🎯 專案目標

- ✅ 提供一套完整的 RESTful API 測試框架實作範例
- ✅ 實作自動測試與覆蓋率分析，提升測試可視性
- ✅ 建立雲端自動化流程，實現零手動部署與測試觸發
- ✅ 探索 DevOps 與測試工程實務工具鏈的整合應用
- ✅ 強化專案結構可讀性與可維護性，利於長期演進

---

## 🧪 使用技術

| 類別        | 技術/工具                                  |
|-------------|---------------------------------------------|
| 語言        | Python 3.11                                 |
| 測試框架    | pytest, pytest-cov                          |
| CI/CD 工具  | GitHub Actions                              |
| 覆蓋率報告  | Coverage (HTML report)                      |
| 部署平台    | GitHub Pages                                |

---

## 📂 專案目錄結構
```
restful-api-test/
├── .github/workflows/
│   └── python-test.yml         # GitHub Actions 工作流程配置
├── assets/
│   └── style.css               # Coverage 報告樣式
├── reports/htmlcov/           # Coverage HTML 報告輸出目錄
├── tests/
│   └── test_api.py             # 測試主程式（含 GET/POST/PUT/DELETE）
├── venv/                      # Python 虛擬環境
├── .gitignore                 # Git 忽略清單
├── README.md                  # 專案說明
├── report.html                # Coverage 主頁轉址檔
├── requirements.txt           # 所需套件清單
```

---

## 🔄 自動化流程設計（CI/CD）

每次程式碼提交至 `main` 分支，GitHub Actions 將自動執行以下流程：

1. 安裝相依套件與環境初始化（`pip install -r requirements.txt`）
2. 使用 `pytest` 執行自動化測試腳本
3. 產生 HTML 覆蓋率報告（透過 `pytest-cov`）
4. 上傳報告目錄為 artifact 並部署至 GitHub Pages

此流程完整採用 GitHub Actions 最新版本模組，支援更佳維護性與相容性，並展現現代化研發環境中測試整合與部署實踐。

---

## 🧪 測試案例內容（test_api.py）

```python
# 測試 GET：查詢用戶列表（應回傳 200 OK）
test_get_users()

# 測試 POST：建立新用戶（應回傳 201 Created）
test_create_user()

# 測試 PUT：更新用戶資料（應回傳 200 OK）
test_update_user()

# 測試 DELETE：刪除用戶（應回傳 204 No Content）
test_delete_user()
```

👉 測試皆使用公開 API 來源：[https://reqres.in/](https://reqres.in/)

測試腳本模擬常見後端資料處理流程，對應現代 API 開發中的資料驗證、狀態碼邏輯與請求結構。

---

## ✅ 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
```

### 2. 本地執行測試並產生報告
```bash
pytest --cov=. --cov-report=html
```

### 3. 查看測試報告
開啟 `htmlcov/index.html` 即可查看視覺化報告（支援覆蓋率熱區追蹤）。

---

## 🌐 線上報告展示

🟢 GitHub Pages：完整測試報告展示：[點我查看](https://hiraeth92.github.io/api-test-ci-cd/)

---

## 🔒 .gitignore 建議內容

```
__pycache__/
.coverage
reports/
venv/
*.pyc
```

---

## 🧩 後續擴充建議

* ✅ 補強錯誤回應與邊界情境測試，提高系統健壯性
* ✅ 導入靜態分析工具（如 SonarCloud）進行程式碼品質審查
* ✅ 整合 API 金鑰與身分驗證場景以模擬權限控管機制
* ✅ 將流程容器化（Docker）利於跨環境部署與測試
* ✅ 結合通訊平台（Slack／Discord）即時通知測試結果與部署狀態

---

## 🙋‍♂️ 作者資訊

* GitHub: [@hiraeth92](https://github.com/hiraeth92)
* Email: [bossun113@gmail.com](mailto:bossun113@gmail.com)

本專案作為自動化測試與流程整合實戰案例，旨在深入理解軟體測試週期、流程設計與品質驗證方法，並探索實務開發中的工程化自動化可能。歡迎討論交流相關經驗。
