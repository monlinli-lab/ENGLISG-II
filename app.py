from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bridge2000 | 國中英單先修戰略站",
    layout="wide",
)

st.title("Bridge2000 | 國中英單先修戰略站")

html_file = Path("index.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=1400, scrolling=True)
else:
    st.error("找不到 index.html，請確認 index.html 與 app.py 位於同一層資料夾。")
