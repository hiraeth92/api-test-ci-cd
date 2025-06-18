# Automated RESTful API Testing with CI/CD

![CI](https://github.com/hiraeth92/api-test-ci-cd/actions/workflows/test.yml/badge.svg)
[![Test Coverage Report](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://hiraeth92.github.io/api-test-ci-cd/)

---

## 📌 專案簡介

本專案旨在展示如何透過 GitHub Actions 建構完整的 API 測試與自動部署流程。透過 `pytest` 撰寫測試案例並使用 `pytest-cov` 產出測試覆蓋率報告，最終自動部署到 GitHub Pages，讓報告可視覺化並公開展示測試品質。

這是一個 CI/CD 自動化實務入門範例，適合想學習 DevOps、SDET（測試自動化工程師）或強化專案維運品質的人使用。

---

## 🎯 專案目標

- 熟悉 RESTful API 測試流程
- 使用 pytest 撰寫自動化測試案例
- 透過 coverage 報告了解測試覆蓋率
- 實作 GitHub Actions 自動測試與部署流程（CI/CD）
- 將測試報告自動部署至 GitHub Pages（可公開瀏覽）

---

## 🧪 使用技術

| 分類         | 技術                            |
|--------------|----------------------------------|
| 語言         | Python 3.11                      |
| 測試框架     | `pytest`, `pytest-cov`           |
| CI/CD 工具   | GitHub Actions                   |
| 報告格式     | Coverage HTML report             |
| 部署         | GitHub Pages                     |

---

## 🛠️ 專案結構說明

```

.
├── .github/workflows/test.yml       # GitHub Actions CI/CD 設定檔
├── requirements.txt                 # 相依套件清單
├── test\_api.py                      # 測試案例 (範例 API 測試)
├── htmlcov/                         # coverage HTML 報告（自動產生）
├── report.html                      # coverage 報告入口（可忽略）
├── .coverage                        # coverage 原始數據（pytest 產出）
└── README.md                        # 專案說明文件


---

## 🚀 快速開始

### 1️⃣ 安裝環境

```bash
pip install -r requirements.txt
````

### 2️⃣ 執行測試

```bash
pytest --cov=. --cov-report=html
```

### 3️⃣ 查看測試報告

打開 `htmlcov/index.html` 即可看到可視化的測試覆蓋率報告。

---

## 🔄 自動化流程（CI/CD）

每次 `push` 到 `main` 分支時，GitHub Actions 會自動執行以下流程：

1. 安裝相依套件（從 `requirements.txt`）
2. 執行測試與 coverage 報告產出
3. 上傳 HTML 測試報告至 GitHub Pages
4. 產出測試徽章與 coverage 狀態頁

### 🔧 workflow 設定（`test.yml`）

使用新版 GitHub Actions 流程：

* 使用 `actions/setup-python@v5`
* 使用 `actions/upload-artifact@v4`、`download-artifact@v4`
* 部署採用新版 `deploy-pages@v4` 並完全移除舊版 v3 套件（已淘汰）

✅ **已符合 2024 年 GitHub Pages 新規範**

---

## 🌐 線上查看 Coverage

👉 [測試報告 GitHub Pages 展示](https://hiraeth92.github.io/api-test-ci-cd/)

---

## 📈 專案成果

* ✅ 測試覆蓋率達 **100%**
* ✅ GitHub Actions 自動部署測試報告
* ✅ 成功避免過時的 Action 套件（如 v3 upload-artifact）
* ✅ README 顯示 CI 與 Coverage 狀態徽章

---

## 🧩 可擴充方向建議

1. ✅ 加入更複雜的 REST API 測試（含 POST/PUT/DELETE）
2. ✅ 整合 Postman 或 Swagger 自動測試匯出
3. ✅ 引入 Codecov、SonarCloud 等外部平台做品質分析
4. ✅ 將測試整合至 Docker 環境
5. ✅ 結合 Slack 或 Discord 發送 CI 通知

---

## 🙋‍♂️ 作者

* GitHub: [@hiraeth92](https://github.com/hiraeth92)
* 歡迎提問、開 issue 或 fork 專案交流！

---

## 📜 License

本專案採用 MIT License 授權，可自由使用與修改。

```

---

如需我幫你直接更新此 `README.md` 檔，或要幫你補上更多圖示與流程圖，也可以提出。這份內容是可以拿去**作品集、履歷、面試展示**用的完整模板。
```
