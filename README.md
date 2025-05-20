# SlopBot
Generate AI content

## Workflow

 - Generate Topic
 - Generate Story (plot)
 - Generate Series of Videos (scenes)
 - Generate Audio
 - Edit Scenes together & Edit Audio together
 - Upload Results
    - Post to Youtube
    - Post to TikToc
    - Post to Instagram
    - Etc

## Setup

To generate a Google API key for Gemini/GenAI:

1. **Go to the [Google AI Studio](https://aistudio.google.com/app/apikey)**
2. **Sign in with your Google account.**
3. **Click "Create API Key"** and follow the prompts.
4. **Copy the generated API key.**

Use this key as the value for the `GOOGLE_API_KEY` environment variable when running your app.  
**Never share your API key publicly.**

## Usage

Build the Docker image:
```sh
docker build -t slopbot .
```

Run the server:
```sh
docker run -p 8000:8000 -e GOOGLE_API_KEY=$GOOGLE_API_KEY slopbot
```
