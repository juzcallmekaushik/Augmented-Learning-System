from bot import (
      os,
      pyautogui,
      sr,
      time,
      pyttsx3,
)

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

def MusicPlay():
      speak("what kind of music would you like to listen?")
      musictype = takecommand().lower()
      os.startfile("C:\\Users\\Kaushik\\AppData\\Roaming\\Spotify\\Spotify.exe")
      time.sleep(2)
      pyautogui.hotkey("ctrl", "l")
      pyautogui.press("backspace")
      time.sleep(2)
      if 'telugu' in musictype:
            pyautogui.typewrite("Latest Telugu")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")
      elif 'tamil' in musictype:
            pyautogui.typewrite("Latest Tamil")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")            
      elif 'hindi' in musictype:
            pyautogui.typewrite("Latest Hindi")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")            
      elif 'japanese' in musictype:
            pyautogui.typewrite("Latest Japanese")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")                      
      elif 'instrumental' in musictype:
            pyautogui.typewrite("Latest Lofi")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")           
      elif 'english' in musictype:
            pyautogui.typewrite("Frequently Played")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")                  
      else:
            pyautogui.typewrite(musictype)
            time.sleep(3)
            pyautogui.keyDown('enter')
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.press("enter")                  
      
      time.sleep(3)
      pyautogui.click(1877, 11)

def MusicStop():
      pyautogui.press('playpause')

def NextMusic():
     pyautogui.press("nexttrack")

def PrevMusic():
     pyautogui.press("prevtrack")