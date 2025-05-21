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

### To generate a Google API key for Gemini/GenAI:

1. **Go to the [Google AI Studio](https://aistudio.google.com/app/apikey)**
2. **Sign in with your Google account.**
3. **Click "Create API Key"** and follow the prompts.
4. **Copy the generated API key.**

Use this key as the value for the `GOOGLE_API_KEY` environment variable when running your app.  
**Never share your API key publicly.**

### To get a RunwayML API key:

1. Go to the [RunwayML website](https://runwayml.com/).
2. Sign up for an account or log in.
3. In your Runway dashboard, click your profile icon (top right) and go to "Account" or "API Keys".
4. Click "Create API Key" or "Generate New Key".
5. Copy the generated API key and use it as the value for the `RUNWAY_API_KEY` environment variable in your project.

### To get your Google Cloud project environment variable (GOOGLE_CLOUD_PROJECT):

1. Go to the [Google Cloud Console](http://console.cloud.google.com/).
2. Select your project at the top of the page.
3. You will see both a Project ID (e.g., my-cool-project-123) and a Project Number (e.g., 123456789012).
4. Set `GOOGLE_CLOUD_PROJECT` to your Project ID (e.g., my-cool-project-123), not the project number.

## Usage

Build the Docker image:
```sh
docker build -t slopbot .
```

Run the server:
```sh
docker run -p 8000:8000 -e GOOGLE_API_KEY=$GOOGLE_API_KEY slopbot
```
