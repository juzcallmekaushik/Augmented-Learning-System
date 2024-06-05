from bot import (
      os,
      pyautogui,
      sr,
      time,
      pyttsx3,
)

from utils.speech import (
      speak
)

from utils.takecommand import (
      takecommand
)

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
      pyautogui.hotkey("alt", "esc")

def MusicStop():
      pyautogui.press('playpause')

def NextMusic():
     pyautogui.press("nexttrack")

def PrevMusic():
     pyautogui.press("prevtrack")