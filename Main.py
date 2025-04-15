import streamlit as st
from PIL import Image

st.set_page_config(page_title="GlonaVox", page_icon="🌍")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;margin-top:-50px;'>🌍 GlonaVox - Speak Beyond Borders 🗣️</h2>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'> Choose Your Translation Mode</h4>", unsafe_allow_html=True)

# Neuomorphic 2x2 grid card styling with color
st.markdown("""
    <style>
        .neu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            /*gap:100px;*/
            
            margin: -100px;
            margin-top: -10px;
        }
        .neu-card {
            border-radius: 20px;
            box-shadow: 9px 9px 16px #bebebe,
                        -9px -9px 16px #ffffff;
            
            padding: 50px;
            height: 150px;
            width: 240px;
            text-align: center;
            transition: 0.3s ease;
            cursor: pointer;
            font-weight: 600;
            font-size: 18px;
        }
        .neu-card:hover {
            box-shadow: inset 9px 9px 16px #bebebe,
                        inset -9px -9px 16px #ffffff;
            transform: scale(1.02);
        }
        .neu-link {
            text-decoration: none;
            color: black;
        }

        .card-yellow { background: #fff9c4; }  /* Light Yellow */
        .card-cyan { background: #b2ebf2; }    /* Light Cyan */
        .card-green { background: #c8e6c9; }   /* Light Green */
        .card-purple { background: #e1bee7; }  /* Light Purple */
    </style>
""", unsafe_allow_html=True)

# Card layout
st.markdown(""" <style>.neu-link {
            text-decoration: none !important;
            color: inherit !important;
        }</style>
    <div class="neu-grid">
        <a href="/Text_to_Text" class="neu-link">
            <div class="neu-card card-yellow">📝<br>Text to Text</div>
        </a>
        <a href="/Audio_to_Text" class="neu-link" >
            <div class="neu-card card-cyan">🎤<br>Audio to Text</div>
        </a>
        <a href="/Text_to_Audio" class="neu-link">
            <div class="neu-card card-green">🗣️<br>Text to Audio</div>
        </a>
        <a href="/Audio_to_Audio" class="neu-link">
            <div class="neu-card card-purple">🔁<br>Audio to Audio</div>
        </a>
    </div>
""", unsafe_allow_html=True)


# Add spacing before About section
st.markdown("<br><br>", unsafe_allow_html=True)

# About GlonaVox section (Not expandable)
st.markdown("""
    <div style='margin-top:40px;margin-left:-100px;margin-right:-110px; padding: 30px; border-radius: 20px; background-color: #f0f4f8; box-shadow: 4px 4px 10px #d0d0d0;'>
        <h3 style='text-align: center;'>🤖 About Me</h3>
        <p style='font-size: 16px; text-align: justify;'>
            Hello! <strong>I’m GlonaVox</strong> — your personal real-time speech translation companion.<br><br>
            I exist to help people connect, understand, and communicate, no matter what language they speak. Whether you're having a live conversation, preparing a presentation, or simply curious about a foreign phrase — I’m here for you.<br><br>
             You can speak to me, type to me, or even upload a recording — I’ll translate it, instantly and expressively.<br><br>
            My mission? To erase language barriers and bring the world a little closer — one word at a time.<br><br>
            So go ahead, speak your language. I’ll make sure the world understands. 🌍
        </p>
    </div>
""", unsafe_allow_html=True)

