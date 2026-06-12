import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=6)

        text = r.recognize_google(audio)
        print("you said:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        # No speech detected within timeout
        print("Timeout: no speech detected")
        return ""

    except sr.UnknownValueError:
        # Speech detected but not understood
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        # Internet or API issue
        print("Speech service error")
        return ""

    except Exception as e:
        print("Listen error:", e)
        return ""


    
