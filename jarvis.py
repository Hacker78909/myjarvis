import os
import subprocess
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyttsx3
import objc

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_website(command):
    websites = {
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
        "linkedin": "https://www.linkedin.com",
        "youtube": "https://www.youtube.com",
        "tiktok": "https://www.tiktok.com",
        "netflix": "https://www.netflix.com",
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
        "snapdeal": "https://www.snapdeal.com",
        "paytm": "https://www.paytm.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "google maps": "https://www.google.com/maps",
        "google drive": "https://drive.google.com",
        "google photos": "https://photos.google.com",
        "google pay": "https://pay.google.com",
        "uber": "https://www.uber.com",
        "ola": "https://www.olacabs.com",
        "zomato": "https://www.zomato.com",
        "swiggy": "https://www.swiggy.com",
        "bookmyshow": "https://www.bookmyshow.com",
        "makemytrip": "https://www.makemytrip.com",
        "irctc": "https://www.irctc.co.in",
        "hdfc bank": "https://www.hdfcbank.com",
        "sbi anywhere": "https://www.onlinesbi.com",
        "icici bank": "https://www.icicibank.com",
        "aniwatch": "https://aniwatch.me",
        "zoro": "https://zoro.to",
        # Add more websites as needed
    }

    if command in websites:
        webbrowser.open(websites[command])
    else:
        print("I'm not sure how to open that. Please check your command.")

def perform_basic_actions(command):
    if "open notepad" in command:
        os.system("notepad")
    elif "open calculator" in command:
        os.system("calc")
    elif "open file explorer" in command:
        os.system("explorer")
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
    else:
        print("I'm not sure how to perform that action. Please check your command.")

def perform_app_actions(command):
    if "open spotify" in command:
        # Add your code to open Spotify
        print("Opening Spotify...")
    elif "play music" in command:
        # Add your code to play music
        print("Playing music...")
    # Add more app-related actions as needed

if __name__ == "__main__":
    speak("Hello, I am your Python assistant. How can I help you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there! How can I assist you?")
        elif "goodbye" in command or "exit" in command:
            speak("Goodbye! Have a great day.")
            break
        elif "your name" in command:
            speak("I am your Python assistant.")
        elif "open" in command:
            open_website(command)
        elif "do" in command:
            perform_basic_actions(command)
        elif "on" in command:
            perform_app_actions(command)
        else:
            print("I didn't understand that command. Please try again.")
