import streamlit as st
from gtts import gTTS
import io

st.title(" حول النص إلى صوت!")

text = st.text_area("اكتب النص هنا:")

lang = st.selectbox("اختار اللغة:", ["عربي", "إنجليزي"])

speed = st.selectbox("اختار سرعة الصوت:", [" سريع", " عادي", " بطيء"])

if st.button("تشغيل الصوت "):
    if text:
        lang_code = "ar" if lang == "عربي" else "en"
        is_slow = speed == " بطيء"
        tts = gTTS(text=text, lang=lang_code, slow=is_slow)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        st.audio(buf, format="audio/mp3")
    else:
        st.warning("اكتب نص أولاً! ")
