import streamlit as st
import speech_recognition as sr
import tempfile
from googletrans import Translator, LANGUAGES
import os
st.set_page_config(page_title="Audio to Text", page_icon="🎤")
st.title("🎤 Audio to Text")
translator = Translator()
language_mapping = {name: code for code, name in LANGUAGES.items()}
def get_code(lang):
    return language_mapping.get(lang, lang)
from_lang = st.selectbox("Source Language", list(LANGUAGES.values()))
to_lang = st.selectbox("Target Language", list(LANGUAGES.values()))
input_method = st.radio("Choose Input Method", ["Real-Time Microphone", "Upload Audio File"])
recognizer = sr.Recognizer()
if input_method == "Real-Time Microphone":
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language=get_code(from_lang))
            translated = translator.translate(text, src=get_code(from_lang), dest=get_code(to_lang))
            st.success(f"Recognized: {text}")
            st.success(f"Translated: {translated.text}")
else:
    uploaded = st.file_uploader("Upload WAV file", type=["wav"])
    if uploaded:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded.read())
            path = tmp.name
        with sr.AudioFile(path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language=get_code(from_lang))
            translated = translator.translate(text, src=get_code(from_lang), dest=get_code(to_lang))
            st.success(f"Recognized: {text}")
            st.success(f"Translated: {translated.text}")
        os.remove(path)