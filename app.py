import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import io

st.title(" حول النص إلى صوت!")

text = st.text_area("اكتب النص هنا:")

lang = st.selectbox("اختار اللغة:", ["عربي", "إنجليزي"])

speed = st.selectbox("اختار سرعة الصوت:", ["سريع", " عادي", " بطيء"])

if st.button("تشغيل الصوت "):
    if text:
        lang_code = "ar" if lang == "عربي" else "en"

        tts = gTTS(text=text, lang=lang_code)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)

        audio = AudioSegment.from_mp3(buf)

        if speed == " سريع":
            audio = audio.speedup(playback_speed=1.5)
        elif speed == " بطيء":
            audio = audio.speedup(playback_speed=0.7)

        out = io.BytesIO()
        audio.export(out, format="mp3")
        out.seek(0)

        st.audio(out, format="audio/mp3")
    else:
        st.warning("اكتب نص أولاً! 😅")
