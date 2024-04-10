from bot import (
    pyttsx3,
    sr,
    pyautogui,
    MONGOLINK,
    pymongo,
    datetime,
    os,
    time,
    win11toast,
    threading,
)

from win11toast import toast
#import main

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
        return query.lower()
    except Exception as e:
        print(e)
        return "none"

def hotword():
    while True:
        wakeword = takecommand().lower()
        if "edwin" in wakeword:
            main_path = "C:\\Users\\Kaushik\\Documents\\Programming\\Augmented-Learning-System\\src\\main.py"
            os.startfile(main_path)

def fetch_tasks():
      client = pymongo.MongoClient(MONGOLINK, server_api=pymongo.server_api.ServerApi("1"), minPoolSize=1)
      timenow = int(time.time()) + 1
      db = client.Edwin
      tasks = db.tasks
      results = tasks.find({"completed": False})
      for result in results:
          if result["time"] <= timenow:
            name = result["reminder"]
            notify("Task Completion Reminder", name)
            tasks.delete_one({"_id": result["_id"]})
            pass
      threading.Timer(120, fetch_tasks).start()

def fetch_reminder():
      client = pymongo.MongoClient(MONGOLINK, server_api=pymongo.server_api.ServerApi("1"), minPoolSize=1)
      timenow = int(time.time()) + 1
      db = client.Edwin
      reminders = db.reminders
      results = reminders.find({"completed": False})
      for result in results:
          if result["time"] <= timenow:
            name = result["reminder"]
            notify("Reminder", name)
            reminders.delete_one({"_id": result["_id"]})
            pass
      threading.Timer(120, fetch_reminder).start()

def notify(title, reminder):
    toast(title=title, body=reminder, icon="C:\\Users\\Kaushik\\Documents\\Programming\\Augmented-Learning-System\\assets\\Logo.ico", duration="long", scenario='incomingCall')

def threadings():
    HotWord = threading.Thread(target=hotword)
    Tasks = threading.Thread(target=fetch_tasks)
    Reminders = threading.Thread(target=fetch_reminder)

    HotWord.start()
    Tasks.start()
    Reminders.start()

def app_startup():
    time.sleep(2)
    pyautogui.hotkey("alt", "f1")
    time.sleep(2)
    threadings()

if __name__ == "__main__":
    app_startup()