
import streamlit as st
import requests
import io
from pydub import AudioSegment
from pydub.playback import play
import tempfile

# Set backend URL - adjust if deployed elsewhere(Fast api url )
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Finance Assistant", layout="centered")

st.title("Multi-Agent Finance Assistant to check about finance related query")

mode = st.radio("Choose input mode:", ("Text", "Voice"))

if mode == "Text":
    user_input = st.text_area("Ask your question here:", height=100)
    if st.button("Send Question"):
        if user_input.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Getting response..."):
                response = requests.post(f"{API_URL}/query-text/", data={"user_input": user_input})
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("### Assistant Response:")
                    st.write(data.get("response", "No response."))
                else:
                    st.error("Error communicating with the server.")

else:  # Voice mode
    audio_file = st.file_uploader("Upload an audio file (wav format preferred)", type=["wav", "mp3", "m4a"])
    if audio_file is not None:
        if st.button("Send Audio"):
            with st.spinner("Processing audio..."):
                files = {"file": (audio_file.name, audio_file, audio_file.type)}
                response = requests.post(f"{API_URL}/query-voice/", files=files)
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("### Transcription:")
                    st.write(data.get("transcript", ""))
                    st.markdown("### Assistant Response:")
                    st.write(data.get("response", ""))
                    # Optional: You can add playback if you extend your API to return audio bytes.
                else:
                    st.error("Error communicating with the server.")
