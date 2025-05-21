import os
from google.cloud import texttospeech


class AudioAgent:
    def __init__(self, gcp_project=None):
        self.gcp_project = gcp_project or os.environ.get("GOOGLE_CLOUD_PROJECT")
        if not self.gemini_api_key or not self.gcp_project:
            raise ValueError("Set GEMINI_API_KEY and GOOGLE_CLOUD_PROJECT env vars.")
        self.tts_client = texttospeech.TextToSpeechClient()

    def generate_audio(self, text, output_path="output_audio.mp3"):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = self.tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        with open(output_path, "wb") as out:
            out.write(response.audio_content)
        return output_path
