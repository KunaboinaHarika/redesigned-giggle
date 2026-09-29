import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 AI Language Translator")
st.write("Translate text instantly across multiple languages with Text-to-Speech support.")

LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Arabic": "ar"
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1)

source_text = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

if st.button("Translate", type="primary"):
    if source_text.strip():
        try:
            src_code = LANGUAGES[source_lang]
            tgt_code = LANGUAGES[target_lang]
            
            translated = GoogleTranslator(source=src_code, target=tgt_code).translate(source_text)
            
            st.subheader("Translated Output:")
            st.success(translated)
            
            tts = gTTS(text=translated, lang=tgt_code)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            st.audio(fp, format="audio/mp3")
            
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter text before clicking translate.")
