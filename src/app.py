from bot import (
      pyttsx3,
      sr,
      time,
      os,
      pyautogui,
      threading,
      psutil,
      subprocess
)

import main

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)

def speak(audio):
      engine.say(audio)
      print(f"Edwin: {audio}")
      engine.runAndWait()

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

def check_and_open_app():
      for process in psutil.process_iter():
            if process.name() == "MinimizeToTray.exe":
                  return True
      subprocess.Popen(["start", " ", "MinimizeToTray.exe"], shell=True)
      return False

def hotword():
      while True:
            hotword = takecommand().lower()
            if "edwin" in hotword:
                  mainfile = "C:\\Users\\Kaushik\\Documents\\Programming\\Augmented Learning System - Edwin\\main.py"
                  appfile = "C:\\Users\\Kaushik\\Documents\\Programming\\Augmented Learning System - Edwin\\app.py"
                  os.startfile(mainfile)
                  time.sleep(3)
                  os.c(appfile)

if __name__ == "__main__":
      check_and_open_app()
      time.sleep
      pyautogui.hotkey("alt", "f1")
      time.sleep(2)
      hotword()