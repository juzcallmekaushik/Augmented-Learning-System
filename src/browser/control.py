from bot import (
      os,
      pyautogui,
      sr,
      time,
      pyttsx3,
      requests,
      pyjokes,
      json,
      webbrowser,
      pymongo,
      MONGOLINK,
      pyperclip
)

from utils.speech import (
      speak
)

from utils.takecommand import (
      takecommand
)

def bored():
    url = "https:/www.boredapi.com/api/activity"
    Data = requests.get(url)
    json_data = Data.json()
    activity_Data = json_data["activity"]
    activity_type = json_data["type"]
    speak(f" i would suggest you to {activity_Data}")

def joke():
    joke = pyjokes.get_joke()
    speak(joke)

def weather():
    api_key = "4eb3d461c23f4e3772366478de1298f2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    ipAdd = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
    geo_requests = requests.get(url)        
    geo_data = geo_requests.json()
    city = geo_data['city']
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        high_temperature = y["temp_max"]
        low_temperature = y["temp_min"]        
        z = x["weather"]
        weather_description = z[0]["description"]
        r = f"Right now, its {weather_description} and {current_temperature - 273.15:.0f} degree celcius, the weather forcast shows that the temperatures can go as high as {high_temperature - 273.15:.0f} degree celcius and as low as {low_temperature - 273.15:.0f} degree celcius"
        speak(r)    
        
def Temperature():
    api_key = "4eb3d461c23f4e3772366478de1298f2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    ipAdd = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
    geo_requests = requests.get(url)        
    geo_data = geo_requests.json()
    city = geo_data['city']
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        high_temperature = y["temp_max"]
        low_temperature = y["temp_min"]        
        z = x["weather"]
        t = f"The Current Temperature is {current_temperature - 273.15:.0f} degree celcius"
        speak(t)	  
        
def location():
    speak("give me a second, tracking down our location now")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
        geo_requests = requests.get(url)        
        geo_data = geo_requests.json()
        city = geo_data['city']
        country = geo_data['country']
        speak(f"sir, i am not sure about the exact location, but we are in {city}, {country}")
    except Exception as e:
        speak("sorry sir, due to network issue, i am not able to track our location.")
        pass	
    
def news():
    url = 'https://newsapi.org/v2/top-headlines?country=my&apiKey=d0849fa7aba4447aac6d4292c08045ed'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
    speak('These were the top headlines, Have a nice day Sir!!..')

def IPaddress():
    ip = requests.get('https://api.ipify.org').text
    speak(f"your ip address is {ip}")

def GitHub():
    speak('opening github...')
    webbrowser.open("github.com")

def Stackoverflow():
    speak("opening stack over flow")
    webbrowser.open("stackoverflow.com")

def YouTube():
    speak('opening youtube...')
    webbrowser.open("youtube.com")

def Instagram():
    speak("ok sir, opening instagram")
    webbrowser.open("www.instagram.com")    

def SearchGoogle(query):
    speak(f"searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def LMS():
    speak("opening BAC's learning management System.")
    webbrowser.open("https://lms.bac.edu.my/user_dashboard")

