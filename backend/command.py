import time
import pyttsx3
import speech_recognition as sr
import eel
from backend.logger import setup_logger

logger = setup_logger()

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 174)
    eel.receiverText(text)

# Expose the Python function to JavaScript

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        eel.DisplayMessage("I'm listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 8)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        
        speak(query)
    except Exception as e:
        print(f"Error recognizing speech: {str(e)}\n")
        speak("Sorry, I couldn't understand what you said. Please try again.")
        return None

    return query.lower()

@eel.expose
def takeAllCommands(message=None):
    if message is None:
        query = takecommand()  # If no message is passed, listen for voice input
        if not query:
            return  # Exit if no query is received
        print(query)
        eel.senderText(query)
    else:
        query = message  # If there's a message, use it
        print(f"Message received: {query}")
        eel.senderText(query)
    
    try:
        if query:
            if "open" in query:
                from backend.feature import openCommand
                openCommand(query)
                return None
            elif "send message" in query or "call" in query or "video call" in query:
                from backend.feature import findContact, whatsApp
                flag = ""
                Phone, name = findContact(query)
                if Phone != 0:
                    if "send message" in query:
                        flag = 'message'
                        speak("What message to send?")
                        query = takecommand()  # Ask for the message text
                    elif "call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                    whatsApp(Phone, query, flag, name)
                return None
            elif "on youtube" in query:
                from backend.feature import PlayYoutube
                PlayYoutube(query)
                return None
            else:
                from backend.feature import chatBot
                response = chatBot(query)
                return response
        else:
            speak("No command was given.")
            return None
    except Exception as e:
        print(f"An error occurred while processing the command: {e}")
        speak("Sorry, I encountered an error while processing your command. Please try again.")
        return None
    
    eel.ShowHood()
