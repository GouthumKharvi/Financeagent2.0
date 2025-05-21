                                                   
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow Streamlit frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query-text/")
async def query_text(user_input: str = Form(...)):
    # Dummy response logic
    response = f"You asked: {user_input}. Here's a helpful financial response!"
    return {"response": response}

@app.post("/query-voice/")
async def query_voice(file: UploadFile = File(...)):
    recognizer = sr.Recognizer()
    audio_bytes = await file.read()
    audio_file = sr.AudioFile(io.BytesIO(audio_bytes))

    try:
        with audio_file as source:
            audio = recognizer.record(source)
            transcript = recognizer.recognize_google(audio)
            response = f"You said: {transcript}. Based on this, here's a financial insight!"
            return {"transcript": transcript, "response": response}
    except Exception as e:
        return {"transcript": "", "response": "Sorry, couldn't process the audio.", "error": str(e)}
