import pyttsx3
import speech_recognition as sr
import pyaudio
import pymongo
import random
import os
import time
from datetime import datetime
import calendar
import pyautogui
import psutil
import ctypes
import cv2
import webbrowser
import requests
import pyjokes
import winshell
import json
import threading
import subprocess
import pyperclip
import win11toast
from dotenv import load_dotenv

load_dotenv()
GEMINIAPI = os.environ.get("GeminiAPI")
MONGOLINK = os.environ.get("MongoDBLink")