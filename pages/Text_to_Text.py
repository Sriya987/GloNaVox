
### pages/text_to_text.py ###
import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="Text to Text", page_icon="📝")
st.title("📝 Text to Text Translation")

translator = Translator()
language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_code(lang):
    return language_mapping.get(lang, lang)

from_lang = st.selectbox("Source Language", list(LANGUAGES.values()))
to_lang = st.selectbox("Target Language", list(LANGUAGES.values()))
input_text = st.text_area("Enter Text to Translate")

if st.button("Translate"):
    from_code = get_code(from_lang)
    to_code = get_code(to_lang)
    try:
        translated = translator.translate(input_text, src=from_code, dest=to_code)
        st.success("Translated Text:")
        st.write(translated.text)
    except Exception as e:
        st.error(f"Translation failed: {e}")
