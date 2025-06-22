# AI Writer

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def spin_text(original_text):
    prompt = f"Rewrite the following book chapter in clear language: {original_text}"
    
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
    
    #retrun result
    return result["choices"][0]["message"]["content"]
