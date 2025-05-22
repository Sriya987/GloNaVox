import streamlit as st
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import tempfile
import os
st.set_page_config(page_title="Audio to Audio", page_icon="🔁")
st.title("🔁 Audio to Audio")
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
input_method = st.radio("Choose Input Method", ["Real-Time Microphone", "Upload Audio File"])
recognizer = sr.Recognizer()
if input_method == "Real-Time Microphone":
    if st.button("Start Recording"):
        try:
            with sr.Microphone() as source:
                st.info("Listening... Speak now")
                audio = recognizer.listen(source, phrase_time_limit=10)
                text = recognizer.recognize_google(audio, language=get_code(from_lang))
                st.success(f"Recognized: {text}")
                
                translated = translator.translate(text, src=get_code(from_lang), dest=get_code(to_lang))
                st.success(f"Translated: {translated.text}")
                
                speak_in_browser(translated.text, get_code(to_lang))
        except Exception as e:
            st.error(f"Recognition or Translation failed: {e}")
else:
    uploaded = st.file_uploader("Upload WAV file", type=["wav"])
    if uploaded:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded.read())
                path = tmp.name
            with sr.AudioFile(path) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language=get_code(from_lang))
                st.success(f"Recognized: {text}")
                translated = translator.translate(text, src=get_code(from_lang), dest=get_code(to_lang))
                st.success(f"Translated: {translated.text}")
                speak_in_browser(translated.text, get_code(to_lang))
            os.remove(path)
        except Exception as e:
            st.error(f"Processing failed: {e}")