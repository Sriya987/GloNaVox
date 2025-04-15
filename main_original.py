### main.py ###

import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="GlonaVox", page_icon="🌍")

# App title
st.title("🌍 GlonaVox - Speak Beyond Borders 🗣️")

# Description
st.markdown("""
### Choose Your Translation Mode
Select one of the options below to proceed.
""")

# Display cards for navigation
cols = st.columns(2)

with cols[0]:
    if st.button("📝 Text to Text", use_container_width=True):
        st.switch_page("pages/Text_to_text.py")
    if st.button("🎤 Audio to Text", use_container_width=True):
        st.switch_page("pages/Audio_to_text.py")

with cols[1]:
    if st.button("🗣️ Text to Audio", use_container_width=True):
        st.switch_page("pages/Text_to_audio.py")
    if st.button("🔁 Audio to Audio", use_container_width=True):
        st.switch_page("pages/Audio_to_audio.py")
