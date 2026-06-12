import os
import time
import pyautogui
import subprocess
from listen import listen  # your voice input function
from voice import speak     # your TTS function
import requests
import pyperclip
import re


GEMINI_API_KEY = "AIzaSyCGw8hMY1L2rWC3h-khI9RjA2vHXtZKLFs"
BASE_DIR = "C:/assistant_files"
os.makedirs(BASE_DIR, exist_ok=True)






def chat(prompt,history=None):
    if history is None:
        history = []

    # For Gemini:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    # Create context with last few messages
    context = "\n".join(history[-5:] + [f"User: {prompt}"])
    
    payload = {
        "contents": [
            {
                "parts": [{"text": context}]
            }
        ],
        "generationConfig": {"temperature":0.7, "maxOutputTokens":512}
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return text.strip()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return "Sorry, I couldn't fetch a response."
    except Exception as e:
        print(f"Connection error: {e}")
        return "Sorry, I couldn't connect to the server."


