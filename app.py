import streamlit as st
from gtts import gTTS
import io
 
st.title(" حول النص إلى صوت!")
 
text = st.text_area("اكتب النص هنا:")
 
lang = st.selectbox("اختار اللغة:", ["عربي", "إنجليزي"])
 
if st.button("تشغيل الصوت "):
    if text:
        lang_code = "ar" if lang == "عربي" else "en"
        tts = gTTS(text=text, lang=lang_code)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        st.audio(buf, format="audio/mp3")
    else:
        st.warning("اكتب نص أولاً ")
 
