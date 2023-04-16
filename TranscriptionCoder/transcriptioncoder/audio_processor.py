# audio_processor.py
import openai
import os

class AudioProcessor:
    def __init__(self, input_audio_file: str):
        self.input_audio_file = input_audio_file

    def transcribe(self) -> str:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        with open(self.input_audio_file, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']
