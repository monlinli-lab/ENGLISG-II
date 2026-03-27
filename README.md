# Bridge2000 | 國中英單先修戰略站

這是可直接上傳到 GitHub 並部署到 Streamlit Community Cloud 的版本。內容依你上傳的頁面整理而成。

## 檔案內容
- `app.py`：Streamlit 主程式
- `index.html`：前端展示頁
- `requirements.txt`：Python 套件需求
- `README.md`：部署說明

## 本機測試
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit
1. 建立 GitHub Repository
2. 把本資料夾內全部檔案上傳到 Repository 根目錄
3. 打開 Streamlit Community Cloud
4. 點 `Create app`
5. Repository 選你的 GitHub 專案
6. Branch 選 `main`
7. Main file path 填 `app.py`
8. 按 `Deploy`

## 注意
- `index.html` 與 `app.py` 必須在同一層
- 此頁面使用外部 CDN 載入 Tailwind CSS 與 Font Awesome
- 部署後需能連網載入外部資源
