from bot import (
    pymongo,
    time,
    MONGOLINK,
    pyttsx3,
)

client = pymongo.MongoClient(MONGOLINK, server_api=pymongo.server_api.ServerApi("1"), minPoolSize=1)
timestamp = round(time.time())

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)

def speak(audio):
      engine.say(audio)
      print(f"Edwin: {audio}")
      engine.runAndWait()

class ClassesDB:
	def __init__(self, client):
		self.client = client
		self.db = self.client.Edwin
		self.classes = self.db.classes

	def new_class(self, day, classname, teacher, time, location):
		self.classes.insert_one({"_id": f"{day}_{timestamp}","class_name": str(classname), "teacher": teacher, "location": location,"class_time": str(time)})
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