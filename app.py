from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IDEA LAB",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 여백과 메뉴를 숨겨 원본 홈페이지에 가깝게 표시
st.markdown(
    """
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp, [data-testid="stAppViewContainer"] {
            background: #f5f6f1;
        }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100%;
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "website.html"

if not html_path.exists():
    st.error("website.html 파일을 app.py와 같은 폴더에 넣어주세요.")
else:
    website_html = html_path.read_text(encoding="utf-8")
    components.html(
        website_html,
        height=3600,
        scrolling=True,
    )
