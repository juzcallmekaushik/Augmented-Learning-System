import speech_recognition as sr
import pyttsx3

import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...", end='\r')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" " * 12, end='\r')
        print("Processing...", end='\r')
        query = r.recognize_google(audio, language='en-in')
        print(" " * 14, end='\r')
        print(f"User: {query}")
      
    except Exception as e:
        return "none"

    query = query.lower()
    return query
