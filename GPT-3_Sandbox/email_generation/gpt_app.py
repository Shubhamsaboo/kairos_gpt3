import app1
import app2
import streamlit as st

st.set_page_config(
    page_title="GPT-3 Sandbox",
    page_icon="🐾",
    layout="centered")

# Pages as key-value pairs
PAGES = {
    "Dashboard": app1,
    "GPT-3 Sandbox": app2
}

st.sidebar.title('Go to:')

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
