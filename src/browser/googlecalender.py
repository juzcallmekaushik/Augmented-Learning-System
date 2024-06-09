import pyttsx3
import os.path
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

from utils.speech import speak

def get_college_events(start_date, end_date):
    creds = None
    credentials_path = "credentials.json"
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    start_time = start.isoformat() + 'Z'
    end_time = end.isoformat() + 'Z'
    events_result = service.events().list(
        calendarId="239c1c5b5ceff0bbd9d88feee537f7dcd0449ed6f6934d567eebedaa3c05ad42@group.calendar.google.com",
        timeMin=start_time,
        timeMax=end_time,
        singleEvents=False).execute()
    events = events_result.get('items', [])

    if not events:
        speak("You have no classes on this date!")
        return None, None

    event_texts = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event['summary']
        start_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")
        event_texts.append(f"You have {summary} class at {start_time}")

    if len(event_texts) == 1:
        speak(event_texts[0])
    else:
        if len(event_texts) == 2:
            speak(" and ".join(event_texts))
        else:
            speak(", ".join(event_texts[:-1]) + f", and {event_texts[-1]}")

    return events[0]['summary'], start_time