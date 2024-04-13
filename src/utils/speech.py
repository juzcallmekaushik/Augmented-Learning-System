import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import subprocess


def speak(data):
    voice = 'en-GB-ThomasNeural'
    path = 'C:\\Users\\Kaushik\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\edge-tts.exe'
    command = f'{path} --voice "{voice}" --text "{data}" --write-media "data.mp3"'

    # Execute the command and suppress output
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    process.communicate()

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    print(f"Edwin: {data}")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()