from bot import (
    pymongo,
    time,
    MONGOLINK,
    pyttsx3,
    datetime,
)

from utils.speech import (
      speak
)

from utils.data import (
    days_names,
)

client = pymongo.MongoClient(MONGOLINK, server_api=pymongo.server_api.ServerApi("1"), minPoolSize=1)
timenow = int(time.time()) + 1


class ClassesDB:
	def __init__(self, client):
		self.client = client
		self.db = self.client.Edwin
		self.classes = self.db.classes

	def new_class(self, day, classname, teacher, time, location):
		self.classes.insert_one({"_id": f"{day}_{timenow}","class_name": str(classname), "teacher": teacher, "location": location,"class_time": str(time)})
		return f"New {classname} class has been added to the Database"

	def get_class(self, classname=None, teacher=None, time=None):
		query = {}

		if classname:
			query["class_name"] = classname
		if teacher:
			query["teacher"] = teacher
		if time:
			query["class_time"] = time

		result = self.classes.find_one(query)
		return result

csdb = ClassesDB(client)

class BookmarkDB:
	def __init__(self, client):
		self.client = client
		self.db = self.client.Edwin
		self.marks = self.db.bookmarks
	
	def add_bookmark(self, name, link):
		self.marks.insert_one({"keyword": name, "link": link})
		speak(f"{name} bookmark saved successfully")
	
	def get_bookmark(self, name):
		result = self.marks.find_one({"keyword": name})
		if result:
			link = result["link"]
			return link
		else:
			speak("No Bookmarks found with that particular name.")

bmdb = BookmarkDB(client)

class RemindersDB:
	def __init__(self, client):
		self.client = client
		self.db = self.client.Edwin
		self.reminders = self.db.reminders	

	def add_reminders(self, reminder, reminder_time, date, day):
		timenow = int(time.time()) + 1
		self.reminders.insert_one({"_id": timenow,
				     		   "date": str(date),
						   "day": str(day),
						   "time": reminder_time,
				     		   "reminder": str(reminder),
						   "completed": False})

rmdb = RemindersDB(client)

class TasksDB:
	def __init__(self, client):
		self.client = client
		self.db = self.client.Edwin
		self.tasks = self.db.tasks	

	def add_tasks(self, task, task_time, date, day):
		timenow = int(time.time()) + 1
		datenow = datetime.now().date()
		daynow = days_names[datetime.now().weekday()][1]
		self.tasks.insert_one({"_id": timenow,
				     		   "date": str(date),
						   "day": str(day),
						   "time": int(task_time),
				     		   "task": str(task),
						   "completed": False})
			
	def get_tasks_by_day(self, date):
		timenow = int(time.time()) + 1
		datenow = datetime.now().date()
		daynow = days_names[datetime.now().weekday()][1]		
		results = self.tasks.find({"completed": False})
		for result in results:
			if result["date"] == date:
				task_name = result["task"]
				task_time = result["time"]
				return task_name, task_time

	def get_tasks_by_time(self, date, start_time, end_time):
		timenow = int(time.time()) + 1
		datenow = datetime.now().date()
		daynow = days_names[datetime.now().weekday()][1]		
		results = self.tasks.find({"completed": False})
		for result in results:
			if result["time"] >= start_time and result["time"] <= end_time:
				task_name = result["task"]
				task_time = result["time"]
				return task_name, task_time

tkdb = TasksDB(client)