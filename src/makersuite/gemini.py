import pyttsx3
import ctypes
import os
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINIAPI = os.environ.get("GeminiAPI")

def main(query):
    genai.configure(api_key=GEMINIAPI)

    generation_config = {
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 10,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    while True:
        convo.send_message(query)
        response = convo.last.text
        response = response.replace('*', '')

        summary = convo.send_message(f"summarize the following into one paragraph: \n\n {response}")
        summary = convo.last.text
        
        return summary
