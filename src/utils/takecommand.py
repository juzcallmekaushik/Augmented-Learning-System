import speech_recognition as sr
import pyttsx3

def takecommand():
      r = sr.Recognizer()
      with sr.Microphone() as source: 
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

      try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
      
      except Exception as e:
            return "none"
      query = query.lower()
      return query