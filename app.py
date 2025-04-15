import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os

# Title
st.title("🌍 Voice Translator with AI 🎙️")

# Language Selection
languages = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "English":"en",
    "Hindi": "hi",
    "Japanese": "ja",
    "Arabic": "ar"
}
target_lang = st.selectbox("Choose target language:", list(languages.keys()))
target_lang_code = languages[target_lang]

# Initialize text
user_text = ""

# Speak Button
if st.button("🎤 Speak Now"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak clearly.")
        audio = recognizer.listen(source)

    try:
        user_text = recognizer.recognize_google(audio)
        st.success(f"Recognized: {user_text}")
    except Exception as e:
        st.warning(f"Speech Recognition failed: {e}")

# Text Input (if not spoken)
if not user_text:
    user_text = st.text_input("💬 Or type your message:")

# If we have text, translate and play
if user_text:
    try:
        # Translate
        translator = Translator()
        translated = translator.translate(user_text, dest=target_lang_code)
        st.write(f"📖 Translated ({target_lang}): {translated.text}")

        # Text to Speech
        tts = gTTS(text=translated.text, lang=target_lang_code)
        tts.save("audio.mp3")

        # Playback
        st.audio("audio.mp3", format="audio/mp3")

    except Exception as e:
        st.error(f"Translation or TTS Error: {e}")



# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# from googletrans import Translator
# import os
# import time

# # UI Title
# st.title("🌍 Voice Translator with AI 🎙️")

# # Language Flags and Names
# languages = {
#     "French": ("fr", "🇫🇷"),
#     "Spanish": ("es", "🇪🇸"),
#     "German": ("de", "🇩🇪"),
#     "Tamil": ("ta", "🇮🇳"),
#     "Hindi": ("hi", "🇮🇳"),
#     "Japanese": ("ja", "🇯🇵"),
#     "Arabic": ("ar", "🇸🇦")
# }

# # Language Selection with Flags
# language_names = [f"{flag} {name}" for name, (code, flag) in languages.items()]
# target_lang_name = st.selectbox("Choose target language:", language_names)
# target_lang_code = languages[target_lang_name.split(' ')[1]][0]  # Extract the language code

# # Record Button
# if st.button("🎤 Speak Now"):
#     # Animated Mic when listening
#     st.image("https://media.giphy.com/media/3o85xI7n61GofPj6S0/giphy.gif", width=100)

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("Listening... Please speak clearly.")
#         audio = r.listen(source)

#         try:
#             # Speech Recognition
#             text = r.recognize_google(audio)
#             st.success(f"Recognized: {text}")

#             # Show loading spinner during translation
#             with st.spinner("Translating..."):
#                 # Translate the text
#                 translator = Translator()
#                 translated = translator.translate(text, dest=target_lang_code)
#                 st.write(f"📖 Translated ({target_lang_name}): {translated.text}")

#             # Convert to speech with loading spinner
#             with st.spinner("Converting to Speech..."):
#                 tts = gTTS(text=translated.text, lang=target_lang_code)
#                 tts.save("audio.mp3")

#             # Play audio with waveform animation
#             st.image("https://media.giphy.com/media/xTiTnQxNU8a2qFHZ9i/giphy.gif", width=150)
#             st.audio("audio.mp3", format="audio/mp3")

#         except Exception as e:
#             st.error(f"Error: {e}")

