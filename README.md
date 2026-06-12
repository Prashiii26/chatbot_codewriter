# chatbot_codewriter


AI Desktop Assistant

A Python-powered desktop assistant that combines voice interaction, AI chat, browser automation, file management, and basic system controls.

Features
Voice input and text-to-speech responses
AI-powered conversations
Code generation from prompts
File and folder management
Google and YouTube search
Website launcher
Screenshot capture
Volume and brightness control
Browser tab management
Shutdown and restart commands
Project Structure
project/
│
├── main.py
├── voice.py
├── listen.py
├── chat.py
├── codeassistant.py
└── assistant_files/
Installation
pip install pyautogui pyttsx3 SpeechRecognition

Install any additional dependencies required by your AI/chat implementation.

Usage

Run the assistant:

python main.py

Activate it using the configured keyword, then issue commands such as:

create folder projects
create file notes
search google python tutorials
open youtube machine learning
volume 50
brightness 70
screenshot
Modules
voice.py

Handles text-to-speech output.

Function:

speak(text)
listen.py

Handles speech recognition and converts voice commands into text.

Function:

listen()
chat.py

Provides conversational AI capabilities and maintains chat history.

Function:

chat(message, history)
codeassistant.py

Generates code from natural language prompts and can automatically type it into an editor.

Function:

write_code_file_and_type(prompt)

Example:

write_code_file_and_type(
    "python program to reverse a string"
)
Main Capabilities
File Management
Create folders
Open folders
Delete folders
Create files
Open files
Delete files
Browser Automation
Open Chrome
Search Google
Open YouTube
Open websites
Close/reopen tabs
Switch between tabs
System Controls
Volume adjustment
Brightness adjustment
Bluetooth toggle
Screenshot capture
Shutdown and restart
AI Features
Natural language conversation
Code generation assistance
Voice feedback
Future Improvements
Fully voice-driven interaction
Offline AI model support
Weather and news integration
Application launcher
Reminder and scheduling features



Personal AI desktop assistant built with Python, automation tools, speech recognition, text-to-speech, and conversational AI.


AUTHOR--PRAKASH RAJ JOSHI
