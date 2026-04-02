import requests
import json

# Local Ollama API
url = "http://localhost:11434/v1/completions"

payload = {
    "model": "deepseek-coder",
    "prompt": "Explain this project in simple terms like I am a beginner.",
    "max_tokens": 500
}

response = requests.post(url, json=payload)

# Extract the model output
model_text = response.json()["choices"][0]["text"]

print(model_text)