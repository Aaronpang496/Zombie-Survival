from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zombie Survival",
    page_icon="🧟",
    layout="centered",
)

st.title("🧟 Zombie Survival")
st.caption(
    "Drag inside the arena to move. Your character fires automatically. "
    "Clear waves and choose upgrades."
)

html = Path(__file__).with_name("game.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
