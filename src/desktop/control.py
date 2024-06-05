from bot import (
    psutil,
    sr,
    time,
    os,
    ctypes,
    cv2,
    pyttsx3,
    pyautogui,
    winshell
)

from utils.speech import (
      speak
)

from utils.takecommand import (
      takecommand
)

def batterypercentage():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    speak(f"The Current battery percentage is {battery_percentage} percent.")
    if battery_percentage <= "50%":
        speak(f"Please Connect Charger as there is {battery_percentage}% only left")
    else:
        return
def chargerconnected():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if plugged:
        speak("the Computer is Charging sir.")

    if not plugged:
        speak("The Computer is Not Charging sir.")

def shutdown():
    speak("are you sure you want to shut down your computer sir?")
    reply = takecommand().lower()
    if "yes" in reply:
        speak('Initializing shutdown protocol ')
        speak('have a great day sir! ')
        os.system("shutdown /s /t 5")
    else:
        speak("shut down cancelled")
        return

def restart():
    speak("Restarting your computer")
    os.system("shutdown /r /t 5")

def lockdown():
    speak("Preparing for Lockdown..")
    ctypes.windll.user32.LockWorkStation()

def screenshot():
    speak("what would you like to name the file")
    name = takecommand().lower()
    speak("ok sir, taking the screenshot right ahead")
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("screenshot taken sir, i have saved it in the Jarvis Code Folder")

def WinCam():
    speak("ok sir, opening WinCam")
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam',img)
        k = cv2.time.sleepKey(50)
        if k==27:
            break;
    cap.release()
    cv2.destroyAllWindows()

def username():
    username = psutil.users()
    for user_name in username:
        first_name = user_name[0]
        speak(f"Sir, this computer is signed to {first_name} as a username.")
        return first_name

def Volumeup():
    pyautogui.press("volumeup")

def Volumedown():
    pyautogui.press("volumedown")

def Volumemute():
    pyautogui.press("volumemute")

def Volumeunmute():
    pyautogui.press("volumemute")

def click():
    pyautogui.click()

def closecurrentwindow():
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
     
def switchtab():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def moveright():
    pyautogui.keyDown("win")
    pyautogui.press("right")
    pyautogui.keyUp("win")

def moveleft():
    pyautogui.keyDown("win")
    pyautogui.press("left")
    pyautogui.keyUp("win")

def ScreenMinimize():
    pyautogui.keyDown("win")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.keyUp("win")
    
def ScreenMaximize():
    pyautogui.keyDown("win")
    pyautogui.press("up")
    pyautogui.keyUp("win")

def allwindowmini():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")

def Explorer():
    pyautogui.keyDown("win")
    pyautogui.press("e")
    pyautogui.keyUp("win")

def Settings():
    pyautogui.keyDown("win")
    pyautogui.press("i")
    pyautogui.keyUp("win")

def screenrefresh():
    pyautogui.keyDown("win")
    pyautogui.keyDown("shift")
    pyautogui.keyDown("ctrl")
    pyautogui.press("b")
    pyautogui.keyUp("win")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("ctrl")

def BrowserReload():
      time.sleep(1)
      pyautogui.hotkey('ctrl', 'r')

def BrowserNewTab():
      time.sleep(1)
      pyautogui.hotkey('ctrl', 't')

def BrowserNewWindow():
      time.sleep(1)
      pyautogui.hotkey('ctrl', 'n')

def BrowserOldTab():
     time.sleep(1)
     pyautogui.hotkey('ctrl', 'shift', 't')

def TaskManager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def Recycle():
    winshell.recycle_bin().empty(confirm = True, show_progress = True, sound = True)
    speak("Recycle Bin Emptied...")     
