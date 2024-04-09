from bot import (
    pyautogui,
    time,
    pyttsx3,
    sr,
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

def set_alarm(tt, Timing, number):
	if number == 8:
		hour = tt[0:2]
		minute = tt[3:5]
		AM_PM = tt[6:8]
	else:
		hour = tt[0:1]
		minute = tt[2:4]
		AM_PM = tt[5:7]
	
	if 'AM' in AM_PM:
		AP = 'A'
	else:
		AP = 'P'
	
	pyautogui.hotkey('alt', 'space')
	pyautogui.typewrite('clock')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(4)
	pyautogui.doubleClick(189, 189)
	time.sleep(1)
	pyautogui.click(1847, 946)
	time.sleep(1)
	pyautogui.typewrite(hour)
	time.sleep(1)
	pyautogui.press('tab')
	time.sleep(1)
	pyautogui.typewrite(minute)
	time.sleep(1)
	pyautogui.press('tab')
	time.sleep(1)
	pyautogui.typewrite(AP)
	pyautogui.press('tab')
	
	speak('To help me better organize your alarms, what name would you like to assign this one?')
	name = takecommand().lower()
	pyautogui.typewrite(name)
	
	speak('Would you like me to repeat the alarm?')
	repeat = takecommand().lower()
	
	if 'yes' in repeat or 'yeah' in repeat or 'none' in repeat or '' in repeat:
		speak('What days would you like the alarm to repeat on?')
		days = takecommand().lower()
		
		if 'and' in days:
			daysrepeat = days.replace(' and ', '\n')
		
		pyautogui.press('tab')
		pyautogui.press('tab')
		
		if 'monday' in daysrepeat:
			pyautogui.press('space')
			time.sleep(2)
		
		if 'tuesday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('space')
			time.sleep(2)
		
		if 'wednesday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('space')
			time.sleep(2)
		
		if 'thursday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('space')
			time.sleep(2)
		
		if 'friday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('space')								
			time.sleep(2)
		
		if 'saturday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('space')
			time.sleep(2)
		
		if 'sunday' in daysrepeat:
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('right')
			pyautogui.press('space')
			time.sleep(2)
		
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('enter')
		
		speak(f'Your alarm has been set for {Timing} and it will be repeated every {days}')	
	else:							
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('enter')
		
		speak(f'Your alarm has been set for {Timing}')
