from fastapi import FastAPI
from pydantic import BaseModel
from generate_topic import TopicAgent

app = FastAPI()
topic_agent = TopicAgent()


class PromptInput(BaseModel):

    @app.post("/generate")
    def generate():
        result = topic_agent.generate_prompt()
        return {"prompts": result}
