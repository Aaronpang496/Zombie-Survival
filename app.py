from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Zombie Survival 2",
    page_icon="🧟",
    layout="centered",
)

st.title("🧟 Zombie Survival 2")
st.caption(
    "Drag to move. Shooting is automatic. "
    "Dodge projectiles and warning lines!"
)

html = Path(__file__).with_name("game.html").read_text(
    encoding="utf-8"
)

components.html(html, height=950, scrolling=True)
