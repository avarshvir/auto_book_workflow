#AI Reviewer

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def review_text(spin_text):
    prompt = f"Review, Improve and Rewrite the book text in good way: {spin_text}"

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "google/gemma-3n-e4b-it:free",
            "messages": [{"role": "user", "content": prompt}]
        })
    )
    
    result = response.json()
    return result["choices"][0]["message"]["content"]
