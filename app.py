"""Streamlit wrapper that serves the Bolo voice-composer concept prototype."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Bolo Voice Composer", page_icon="🎙️", layout="wide")

st.markdown(
    "<style>.block-container{padding-top:1rem;padding-bottom:0;max-width:1100px}"
    "header,footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("bolo.html").read_text(encoding="utf-8")
components.html(f"<!doctype html><html><head><meta charset='utf-8'></head><body>{html}</body></html>",
                height=980, scrolling=True)
