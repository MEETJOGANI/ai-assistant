import os
import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *
from backend.logger import setup_logger
import pygame
import webbrowser

logger = setup_logger()

# Initialize pygame mixer
pygame.mixer.init()

def start():
    print("Starting Jarvis...")

    # Initialize eel and frontend directory
    eel.init("frontend")
    print("Eel initialized")

    # Play sound on start
    play_assistant_sound()
    print("Assistant sound played")

    # Define the init function to handle the authentication and further actions
    @eel.expose
    def init():
        print("Initializing Face Authentication...")
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        
        # Start face authentication process
        try:
            flag = recoganize.AuthenticateFace()
        except Exception as e:
            print(f"Error during face authentication: {e}")
            speak("An error occurred during face authentication. Please try again.")
            return
        if flag == 1:
            print("Face recognized successfully")
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to Your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            print("Face not recognized")
            speak("Face not recognized. Please try again")
    
    # Open the frontend via XAMPP's localhost URL (using port 80443)
    # print("Opening the browser...")
    # webbrowser.open('http://localhost:80443/Jarvis-2025-master/frontend/index.html')
    
    # Start the eel application with blocking mode set to True
    eel.start("index.html", mode="chrome", host="localhost", port=8090, block=True)

def play_assistant_sound():
    # Use the absolute path to the sound file directly
    sound_file = "C:\\xampp\\htdocs\\Jarvis-2025-master\\frontend\\assets\\audio\\start_sound.mp3"
    
    # Debugging: Print the file path to ensure it's correct
    print(f"Loading sound from: {sound_file}")
    
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

if __name__ == "__main__":
    start()
