from bot import (
      pyttsx3,
      pyaudio,
      sr,
      random,
      os,
      time,
      datetime,
      calendar,
      pyautogui,
      webbrowser,
)
from utils.data import (
      updated_keywords,
)
from makersuite import (
      gemini,
)

from utils.speech import (
      speak
)

from utils.takecommand import (
      takecommand
)

def ReadEmails():
      speak("opening gmail")
      webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
          
          
def WriteEmails():
      speak("Input the following details")
      q1 = input("Recipient: ")
      q2 = input("Subject: ")
      email_query = f"write an email to {q1} about {q2}"
      email_response = gemini.main(email_query)
      pyautogui.hotkey("alt", "space")
      time.sleep(2)
      pyautogui.typewrite("Notepad")
      pyautogui.press("enter")
      time.sleep(2)
      pyautogui.typewrite(email_response)
      time.sleep(1)
      speak("The email is ready for your review.")