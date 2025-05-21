from fastapi import FastAPI
from pydantic import BaseModel
from generate_topic import TopicAgent
from generate_scene import SceneAgent
from generate_audio import AudioAgent

app = FastAPI()
topic_agent = TopicAgent()


class Server(BaseModel):

    @app.post("/generate")
    def generate():
        result = topic_agent.generate_topic()
        return {"prompts": result}
