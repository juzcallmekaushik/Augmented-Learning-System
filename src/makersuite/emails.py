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

from simplegmail import Gmail
from simplegmail.query import construct_query

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