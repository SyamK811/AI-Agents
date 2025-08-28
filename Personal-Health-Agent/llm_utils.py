# llm_utils.py
import requests

def call_llm(prompt, model="mistralai/mixtral-8x7b-instruct", api_key="......."):    #api-key is hidden for safety purposes
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return f"LLM error: {response.text}"
