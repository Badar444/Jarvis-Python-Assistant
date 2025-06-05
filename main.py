# -------------------------------
# JARVIS - Voice Assistant in Python
# Created by Badar Munir
# Description: Listens to voice commands, opens websites, plays videos, and answers questions via OpenRouter AI API.
# -------------------------------

import speech_recognition as sr         # For voice recognition
import webbrowser                       # To open websites
import pyttsx3                          # For text-to-speech
import socialplayer                     # Custom module to store video links
from openrouter_api import ask_openrouter  # Your API module for OpenRouter calls

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Speak function
def speak_meth(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

# Query OpenRouter AI
def ap(prompt):
    """Sends prompt to OpenRouter AI and returns the reply"""
    reply = ask_openrouter(prompt)
    return reply

# Process user's spoken commands
def processCommand(c):
    """Processes the command and performs relevant actions"""
    print(c)

    # Open websites
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    # Play Video from dictionary
    elif c.lower().startswith("play"):
        video = " ".join(c.lower().split(" ")[1:])  # Get full name like "python basics"
        link = socialplayer.video_links.get(video)
        if link:
            webbrowser.open(link)
        else:
            speak_meth(f"Sorry, I couldn't find a video for '{video}'")


    # Tell a joke
    elif "joke" in c.lower():
        output = ap("Tell me a joke")
        print("Jarvis:", output)
        speak_meth(output)

    # General AI response
    else:
        output = ap(c)
        print("Jarvis:", output)
        speak_meth(output)

# Main loop
if __name__ == "__main__":
    speak_meth("Welcome! to Jarvis. Wait for a second")

    r = sr.Recognizer()
    m = sr.Microphone()

    # Noise calibration
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while True:
        try:
            # Listen for wake word
            print("Say something!")
            with m as source:
                audio = r.listen(source)

            word = r.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak_meth("Ya")

                # Now listen for command
                print("Jarvis is activated. Now say something")
                with m as source:
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Recognition not successful!")
        except sr.RequestError as e:
            print(f"Couldn't request results; {e}")