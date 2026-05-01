import streamlit as st
from gtts import gTTS
import numpy as np
import soundfile as sf
import io

st.title("🎙️ حول النص إلى صوت!")

text = st.text_area("اكتب النص هنا:")
lang = st.selectbox("اختار اللغة:", ["عربي", "إنجليزي"])
speed = st.selectbox("اختار سرعة الصوت:", ["سريع", "عادي", "بطيء"])

def change_speed(audio_bytes, speed_factor):
    buf = io.BytesIO(audio_bytes)
    data, samplerate = sf.read(buf)
    indices = np.arange(0, len(data), speed_factor)
    indices = indices[indices < len(data)].astype(int)
    new_data = data[indices]
    out = io.BytesIO()
    sf.write(out, new_data, samplerate, format='WAV')
    out.seek(0)
    return out

if st.button("تشغيل الصوت ▶️"):
    if text:
        lang_code = "ar" if lang == "عربي" else "en"
        tts = gTTS(text=text, lang=lang_code)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)

        if speed == "بطيء":
            out = change_speed(buf.read(), 0.5)
            st.audio(out, format="audio/wav")
        elif speed == "سريع":
            out = change_speed(buf.read(), 2.0)
            st.audio(out, format="audio/wav")
        else:
            st.audio(buf, format="audio/mp3")
    else:
        st.warning("اكتب نص أولاً! ")
