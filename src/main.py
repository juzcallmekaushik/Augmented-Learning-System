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
      pyperclip,
      webbrowser,
)
import app
from utils.data import (
      updated_keywords,
	HelloResponses,
)
from makersuite import (
      emails,
      gemini,
)

from clock import (
      alarm,
      focus,
      reminders,
)

from browser.control import (
      joke, 
      bored,
      location,
      weather,
      Temperature,
      news,
      IPaddress,
      GitHub, 
      Stackoverflow, 
      YouTube, 
      Instagram,
      SearchGoogle,
      LMS,
)

from browser.spotify import (
      MusicPlay,
      MusicStop,
      NextMusic,
      PrevMusic,
)

from desktop.control import (
      batterypercentage,
      lockdown,
      restart,
      shutdown,
      screenrefresh,
      screenshot,
      switchtab,
      ScreenMaximize,
      ScreenMinimize,
      Settings,
      Recycle,
      BrowserReload,
      Explorer,
      TaskManager,
      BrowserNewTab,
      BrowserOldTab,
      username,
      allwindowmini,
      chargerconnected,
      closecurrentwindow,
      Volumedown,
      Volumemute,
      Volumeunmute,
      Volumeup,
      BrowserNewWindow,
      moveleft,
      moveright,
)

from utils.mongodb import (
      bmdb,
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

def greet():
      hour = int(datetime.now().hour)
      if hour >= 0 and hour < 12:
            speak('Good Morning Sir')

      elif hour >= 12 and hour < 18:
            speak('Good Afternoon Sir')

      else:
            speak('Good Evening Sir')

def getDate():
    present = datetime.now() 
    my_date = datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    year = int(datetime.now().year)
    monthNum = present.month
    dayNum = present.day
    yearNum = (datetime.now().strftime("%Y"))

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                      '26th', '27th', '28th', '29th', '30th', '31st']
    
    speak("Today's date is " + weekday + ". " + ordinalNumbers[dayNum - 1] + " " + month_names[monthNum - 1] + " " + yearNum)

def currenttime():
    time = datetime.now().strftime('%I:%M %p')
    speak(f"the current time is {time}.")

def RunEdwin():
      speak(random.choice(HelloResponses))
      while True:
            query = takecommand().lower()
            result = any(keyword in query for keyword in updated_keywords)
            if result:
                  if "time" in query:
                        currenttime()
                        

                  if "date" in query:
                        getDate()
                        

                  if "email" in query:
                        if "write" in query:
                              emails.WriteEmails()
                              
                        if "show" in query:
                              emails.ReadEmails()
                              

                  if "music" in query or "song" in query:
                        if "play" in query or "start" in query:
                              MusicPlay()
                                                            
                        if "stop" in query:
                              MusicStop()
                              
                        if "next" in query:
                              NextMusic()
                              
                        if "previous" in query:
                              PrevMusic()
                              

                  if "weather" in query:
                        weather()
                        

                  if "temperature" in query:
                        Temperature()
                        

                  if "location" in query or "where am i" in query:
                        location()
                        

                  if "news" in query:
                        news()
                        

                  if "battery percentage" in query:
                        batterypercentage()
                        

                  if "ip address" in query:
                        IPaddress()
                        

                  if "restart" in query:
                        restart()
                        

                  if "shutdown" in query:
                        shutdown()
                        

                  if "lock" in query:
                        lockdown()
                        

                  if "screenshot" in query:
                        screenshot()
                        

                  if "switch tab" in query:
                        switchtab()
                        

                  if "refresh the screen" in query:
                        screenrefresh()
                        

                  if "maximize window" in query or "maximise window" in query:
                        ScreenMaximize()
                        

                  if "minimize window" in query or "minimise window" in query:
                        ScreenMinimize()
                        

                  if "settings" in query:
                        Settings()
                        

                  if "recycle bin" in query:
                        Recycle()
                        

                  if "reload tab" in query:
                        BrowserReload()
                        

                  if "file explorer" in query:
                        Explorer()
                        

                  if "task manager" in query:
                        TaskManager()
                        

                  if "new tab" in query:
                        BrowserNewTab()
                        

                  if "old tab" in query:
                        BrowserOldTab()
                        

                  if "username" in query:
                        username()
                        

                  if "show desktop" in query:
                        allwindowmini()
                        

                  if "charger connected" in query:
                        chargerconnected()
                        

                  if "close the current window" in query:
                        closecurrentwindow()
                        

                  if "volume down" in query:
                        Volumedown()
                        

                  if "volume mute" in query:
                        Volumemute()
                        

                  if "volume unmute" in query:
                        Volumeunmute()
                        

                  if "volume up" in query:
                        Volumeup()
                        

                  if "new brower window" in query:
                        BrowserNewWindow()
                        

                  if "move left" in query:
                        moveleft()
                        

                  if "move right" in query:
                        moveright()
                        
                  
                  if "github" in query:
                        GitHub()
                        

                  if "stackoverflow" in query:
                        Stackoverflow()
                        

                  if "youtube" in query:
                        YouTube()
                        

                  if "instagram" in query:
                        Instagram()
                        

                  if "lms" in query or "college website" in query:
                        LMS()
                        

                  if "search for" in query or "find" in query or "show me" in query:
                        topic = query.replace("search for ", "")
                        topic = query.replace("find ", "")
                        topic = query.replace("show me ", "")
                        SearchGoogle(topic)
                        

                  if "alarm" in query:
                        if 'edwin' in query:
                              TT = query.replace('edwin', '')
                        else:
                              TT = query
                        
                        if 'for' in query:
                              tt1 = TT.replace('set an alarm for ', '')
                        else:
                              tt1 = TT.replace('set an alarm at ', '')
                        
                        tt = tt1.replace('.', '')
                        Timing = tt.upper()
                        number = len(Timing)
                        alarm.set_alarm(tt, Timing, number)
                        
                  
                  if "focus session" in query or "study session" in query:
                        duration1 = ""
                        if "start a focus session" in query: 
                              duration1 = query.replace("start a focus session for ", "")
                        if "start a study session" in query: 
                              duration1 = query.replace("start a study session for ", "")
                        if "hour" in duration1:
                              if "hours" in duration1: 
                                    min = int(duration1.replace("hours", ""))
                              else: 
                                    min = int(duration1.replace("hour", ""))
                              minutes = min * 60
                        focus.focus_sessions(f"{minutes} minutes")
                        

                  if 'open' in query:
                        if "bookmark" not in query:
                              openappname = query.replace('edwin ', '')
                              openapp = openappname.replace('open ', '')
                              pyautogui.hotkey('alt', 'space')
                              time.sleep(1)
                              pyautogui.typewrite(openapp)
                              time.sleep(1)
                              pyautogui.press('enter')
                              
                  if 'close' in query:
                        closeappname = query.replace('close', '')
                        speak("Closing " + closeappname)
                        os.system(f"taskkill /im {closeappname}.exe")	
                        

                  if 'standby' in query or "power-saving mode" in query or "hibernation" in query:
                        speak("initiating hibernation mode..")
                        speak("wake me up whenever you need anything")
                        mainfile = "C:\\Users\\Kaushik\\Documents\\Programming\\Augmented Learning System - Edwin\\src\\app.py"
                        os.startfile(mainfile)
                        time.sleep(3)
                        pyautogui.hotkey('alt', 'f1')
                        time.sleep(2)
                        pyautogui.hotkey('alt', 'f4')

                  elif "bookmark" in query:
                        if "site" in query or "website" in query:
                              name = input("what would you like to save it as: ")
                              time.sleep(2)
                              pyautogui.hotkey("ctrl", "l")
                              pyautogui.hotkey("ctrl", "a")
                              pyautogui.hotkey("ctrl", "c")
                              link = pyperclip.paste()
                              bmdb.add_bookmark(name, link)
                        if "open" in query:
                              name = input("what is the name of the bookmark?")
                              link = bmdb.get_bookmark(name)
                              webbrowser.open_new_tab(url=link)
            else:
                  ai = gemini.main(query)
                  speak(ai)
                  
if __name__ == '__main__':
      RunEdwin()