import streamlit as st
import streamlit.components.v1 as components

# 1. Configure the page
st.set_page_config(
    page_title="Zombie Survival",
    page_icon="🧟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit UI (Header, Footer, Toolbar)
# This makes the game look like a real standalone app
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #05080d; }
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    iframe { border: none; }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Load the game HTML
# Make sure your HTML file is named game.html and is in the same folder as this app.py
try:
    with open("game.html", "r", encoding="utf-8") as f:
        game_html = f.read()
except FileNotFoundError:
    st.error("Error: Could not find 'game.html'. Please make sure the file is in the same folder as app.py.")
    st.stop()

# 4. Display the game with a fixed height
# The height here (720) is slightly taller than the game (700) to give it breathing room
components.html(game_html, height=720, scrolling=False)
