# 🎙️ Jarvis - Python Voice Assistant

Jarvis is a Python-based voice assistant that listens for the word "Jarvis", then responds to voice commands like opening websites, playing videos, telling jokes, and answering questions using OpenRouter AI — a free alternative.

---

## 📦 Features

- 🎧 Voice-activated with the keyword **"Jarvis"**
- 🌐 Opens websites like Google, YouTube, Instagram, etc.
- 📺 Plays videos using a custom video links file
- 🤖 AI chat support using **OpenRouter API**
- 🗣️ Speaks back using text-to-speech

---

## 📂 Project Structure

| File                | Purpose                                         |
|---------------------|-------------------------------------------------|
| `main.py`           | Main voice assistant logic                      |
| `openrouter_api.py` | Connects to OpenRouter AI                       |
| `socialplayer.py`   | Contains Naat names and YouTube video links     |
| `requirements.txt`  | All Python package dependencies                 |
| `README.md`         | Project instructions and documentation          |

---

## 🚀 How to Run

### 1. ✅ Prerequisites

- Python 3.8 or higher
- Microphone access
- Free OpenRouter API key

---

### 2. 🔑 Get OpenRouter API Key

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Create a free account
3. Copy your API key
4. Paste it inside `openrouter_api.py`:

```python
API_KEY = "your_openrouter_api_key_here"