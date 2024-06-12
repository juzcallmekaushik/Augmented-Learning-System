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
    psutil,
)

from win11toast import toast
import platform
from utils.takecommand import (
      takecommand
)

client = pymongo.MongoClient(MONGOLINK, server_api=pymongo.server_api.ServerApi("1"), minPoolSize=1)
db = client.Edwin

global selected_voice

def check_instance(appname):
    if appname in (i.name() for i in psutil.process_iter()):
        return True
    else:
        return False
    
def hotword():
    base_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    main_path = f"{base_dir}//main.py"  
    while True:
        wakeword = takecommand().lower()  
        if "edwin" in wakeword:
            if not check_instance("main.py"):
                os.startfile(main_path)
 
def fetch_tasks():
      timenow = int(time.time()) + 1
      tasks = db.tasks
      results = tasks.find({"completed": False})
      for result in results:
          if result["time"] <= timenow:
            name = result["task"]
            notify("Task Completion Reminder", name)
            tasks.delete_one({"_id": result["_id"]})
            pass
      threading.Timer(120, fetch_tasks).start()

def fetch_reminder():
      timenow = int(time.time()) + 1
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