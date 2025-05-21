import os
import requests


class SceneAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("RUNWAY_API_KEY")
        if not self.api_key:
            raise ValueError("RUNWAY_API_KEY environment variable not set.")

        self.api_url = (
            "https://api.runwayml.com/v1/generate"
        )  # RunwayML Gen-2 endpoint

    def generate_video(
        self, prompt: str = "A sailor talking about the sea."
    ) -> str:
        """
        Generates a video file from a prompt using RunwayML Gen-2.
        Returns the path to the saved video file.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "num_frames": 48,  # ~2 seconds at 24fps
            "width": 512,
            "height": 512,
            "seed": None
        }
        response = requests.post(
            self.api_url, json=payload, headers=headers
        )
        response.raise_for_status()
        result = response.json()
        video_url = result.get("video") or result.get("video_url")
        if not video_url:
            raise RuntimeError("No video URL returned from RunwayML API.")
        video_path = "output_video.mp4"
        self._download_file(video_url, video_path)
        return video_path

    def _download_file(self, url, dest_path):
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
