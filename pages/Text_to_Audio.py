import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import tempfile
st.set_page_config(page_title="Text to Audio", page_icon="🗣️")
st.title("🗣️ Text to Audio")
translator = Translator()
language_mapping = {name: code for code, name in LANGUAGES.items()}
def get_code(lang):
    return language_mapping.get(lang, lang)
def speak_in_browser(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Speech Synthesis Error: {e}")
from_lang = st.selectbox("Source Language", list(LANGUAGES.values()))
to_lang = st.selectbox("Target Language", list(LANGUAGES.values()))
input_text = st.text_area("Enter Text to Speak")
if st.button("Speak"):
    from_code = get_code(from_lang)
    to_code = get_code(to_lang)
    try:
        translated = translator.translate(input_text, src=from_code, dest=to_code)
        st.success("Translated Text:")
        st.write(translated.text)
        speak_in_browser(translated.text, to_code)
    except Exception as e:
        st.error(f"Translation failed: {e}")