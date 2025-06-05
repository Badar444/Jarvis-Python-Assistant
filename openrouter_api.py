import requests

API_KEY = "YOUR_API_KEY_HERE"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "X-Title": "Jarvis Assistant"
}

url = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(prompt):
    data = {
        "model": "meta-llama/llama-4-maverick:free", # ✅ Valid free model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }


    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"