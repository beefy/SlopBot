import os
from google import genai


class TopicAgent:
    def __init__(self, model=None):
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        self.client = genai.Client(api_key=api_key)
        self.model = model or "gemini-2.0-flash-001"

    def generate_prompt(self, topic: str = "urban legends", tone: str = "suspenseful") -> str:
        user_prompt = f"Generate 3 engaging TikTok-style storytelling topics about {topic} in a {tone} tone."
        response = self.client.models.generate_content(
            model=self.model,
            contents=user_prompt,
        )
        return response.text
