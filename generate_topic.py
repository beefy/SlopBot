from google.generativeai.agent import Agent
from google.generativeai.chat_models import ChatModel
from google.generativeai.types import TextPrompt


class TopicAgent(Agent):

    def init(self, model=None):
        super().init()
        self.model = model or ChatModel(model="gemini-pro")

    def generate_prompt(self, topic: str, tone: str = "suspenseful") -> str:
        user_prompt = "Generate 3 engaging TikTok-style storytelling topics."
        response = self.model.chat(TextPrompt(user_prompt))
        return response.text


if __name__ == "main":
    agent = TopicAgent()
    prompts = agent.generate_prompt("urban legends")
    print(prompts)
