import requests

API_KEY = "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"
# your_openrouter_api_key_here
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # "HTTP-Referer": "https://yourproject.com",  # Replace with your own URL or GitHub repo
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


