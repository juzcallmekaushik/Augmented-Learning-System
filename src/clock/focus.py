from bot import (
    pyautogui,
    time,
    pyttsx3,
    sr,
    os,
    webbrowser,
    winreg
)

from utils.speech import (
      speak
)

from utils.takecommand import (
      takecommand
)

def focus_sessions(duration):
      os.startfile("C:\\Users\\Kaushik\\AppData\\Roaming\\Spotify\\Spotify.exe")
      time.sleep(2)
      pyautogui.hotkey("ctrl", "l")
      pyautogui.press("backspace")
      time.sleep(2)	
      pyautogui.typewrite("Latest Lofi")
      time.sleep(3)
      pyautogui.press("enter")
      pyautogui.press("tab")
      pyautogui.press("tab")
      pyautogui.press("tab")
      time.sleep(2)
      pyautogui.press("enter") 
      time.sleep(3)
      pyautogui.click(1877, 11)
      time.sleep(1)      
      focus_timers_dir = "C:\\Users\\Kaushik\\Documents\\Programming\\Augmented Learning System - Edwin\\assets\\focus_timers"
      durations_mapping = {
            "60 minutes": "60",
            "75 minutes": "75",
            "90 minutes": "90",
            "105 minutes": "105",
            "120 minutes": "120",
            "135 minutes": "135",
            "150 minutes": "150",
            "165 minutes": "165",
            "180 minutes": "180"
      }

      if duration in durations_mapping:
            timer_file = os.path.join(focus_timers_dir, f"{durations_mapping[duration]} minutes.mp4")
            if os.path.exists(timer_file):
                  os.startfile(timer_file)
                  time.sleep(2)
                  pyautogui.press("space")
                  pyautogui.doubleClick(951, 632)
                  speak(f"{duration} focus session timer opened. click on the space bar to begin the session!")
            else:
                  print(f"Focus timer file for {duration} not found.")
      else:
            print("Invalid duration.")