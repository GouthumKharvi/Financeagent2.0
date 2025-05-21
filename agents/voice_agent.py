
import speech_recognition as sr
import pyttsx3

class VoiceAgent:
    def __init__(self):
        # Initialize speech recognizer and TTS engine
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def speech_to_text(self, audio_file_path):
        """
        Convert speech audio file to text using SpeechRecognition (Google Web Speech API).

        Args:
            audio_file_path (str): Path to audio file (wav format recommended).

        Returns:
            str: Transcribed text or error message.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio)
            return text
        except Exception as e:
            return f"Error in speech-to-text: {str(e)}"

    def text_to_speech(self, text):
        """
        Convert input text to speech and play it.

        Args:
            text (str): Text to be spoken aloud.
        """
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {str(e)}")
