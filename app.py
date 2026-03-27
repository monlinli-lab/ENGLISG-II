import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bridge2000 | 國中英單會考戰略站",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 100%;
    }
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

HTML_CODE = r