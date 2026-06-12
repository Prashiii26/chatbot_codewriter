# code_assistant.py
import os
import time
import pyautogui
import subprocess
from listen import listen  # your voice input function
from voice import speak     # your TTS function
import requests
import pyperclip
import re


# Gemini API key
GEMINI_API_KEY = "YOUR API KEY"
BASE_DIR = "C:/assistant_files"
os.makedirs(BASE_DIR, exist_ok=True)



def generate_code(prompt,lang="python"):
    """Generate Python code using the confirmed gemini-2.5-flash model"""
    
    # 1. Use the model ID found in your list
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    # 2. Fix the payload structure (Gemini uses 'contents' and 'parts')
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Write only {lang} code for: {prompt}. Do not include markdown backticks or explanations."
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 4096
                            }
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            # 3. Fix the data path to extract the text
            # Path: data -> candidates -> content -> parts -> text
            code_text = data["candidates"][0]["content"]["parts"][0]["text"]
            
            # Remove any accidental markdown backticks (```python)
            clean_code = code_text.replace("```python", "").replace("```", "").strip()
            return clean_code
        else:
            print(f"Error {response.status_code}: {response.text}")
            return ""
            
    except Exception as e:
        print(f"Connection Error: {e}")
        return ""
    


def write_code_file_and_type(user_input):
    """Main function to get voice prompt, generate code, save file, open VS Code, and type code"""
    

    
    prompt = user_input
    if not prompt:
        speak("Sorry, I didn't hear anything.")
        return
    
    languages={"python":".py", "c":".c","cpp":".cpp","js":".js"}
    selected_lang="python"
    ext=".py"
    
    words=prompt.lower().split()
    for lang in languages:
        if lang in words:
            selected_lang=lang
            ext=languages[lang]
            prompt=prompt.replace(f"in {lang}","").strip()
            break 
           

    speak("Generating your code...")
    code = generate_code(prompt,selected_lang)
    if not code:
        speak("Could not generate the code.")
        return

    # Step 1: Save to a .py file
    prompt = re.sub(r'[^a-zA-Z0-9_]', '', prompt.replace(" ", "_"))
    filename = os.path.join(BASE_DIR, prompt + ext)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    
    speak("should i open and run it?")
    confirm=input().lower()
    if confirm=="yes":
        speak("Opening VS Code...")
        subprocess.Popen(["code", filename], shell=True)
        time.sleep(5)  # wait for VS Code to open
        speak("sir i have written the code in vs code")

        speak("Running the generated code now...")



        try:
           if selected_lang == "python":
              subprocess.Popen(["python", filename], shell=True)
              speak("Python code executed.")

           elif selected_lang == "js":
               subprocess.Popen(["node", filename], shell=True)
               speak("JavaScript code executed.")

           elif selected_lang == "c":
               exe_file = filename.replace(".c", ".exe")
               subprocess.Popen(
                f"gcc {filename} -o {exe_file} && {exe_file}",
                shell=True
                )
               speak("C program compiled and executed.")

           elif selected_lang == "cpp":
              exe_file = filename.replace(".cpp", ".exe")
              subprocess.Popen(
              f"g++ {filename} -o {exe_file} && {exe_file}",
              shell=True
                )
              speak("C plus plus program compiled and executed.")

           else:
              speak("Code generated but not executed.")

        except Exception as e:
           speak(f"Error running code: {e}")





       
    
      

    # Step 3: Simulate typing the code
    
    # width, height = pyautogui.size()
    # pyautogui.click(width / 2, height / 2)
    # time.sleep(0.5)
    # #focusing cursor
    # pyautogui.hotkey('ctrl', 'home') 
    # time.sleep(0.2)
    # # Optional: Clear the file before typing so it's not duplicated
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.press('backspace')
    # pyperclip.copy(code)
    # pyautogui.hotkey('ctrl', 'v')
    # # pyautogui.typewrite(code, interval=0.01)
    # speak("code is written ")

   
