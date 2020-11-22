import os
import sys
import re
import random
import datetime
import pyaudio
import webbrowser
import pyscreenshot
import speech_recognition as sr
import wikipedia
import pyttsx3
import requests
import json
import psutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello I am Lia. Please tell me how can I help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except sr.UnknownValueError:
        print("Say that again please...")
        speak("Say that again please...")
        query = takecommand()

    return query

def battery():    
    battery = psutil.sensors_battery()
    print(f"Battery is at {battery.percent} %")
    speak("Battery is at")
    speak(battery.percent )

def screenshot():
    img = pyscreenshot.grab()
    img.show()
    img.save("ss.png")

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'who are you' in query:
            speak("Hello, I am Lia Version 1.O, a python interpreted voice assistant. I am here to help you.")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open' in query:
            websites = re.search('open (.+)', query)
            if websites:
                domain = websites.group(1)
                print(domain)
                url = 'http://www.' + domain + ".com"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)
                speak("Requested website has been opened by me.")
            else:
                pass

        elif "where is" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            query = query.split(" ")
            location = query[2]
            speak("Hold on , I will show you where " + location + " is.")
            webbrowser.get('chrome').open("https://www.google.nl/maps/place/" + location)

        elif 'folder' in query:
            speak("What's the folder name?")
            folder_name = takecommand()
            downloadsPath = "C:\\Users\\amant\\" + folder_name
            os.startfile(downloadsPath)

        elif 'your creator' in query:
            speak("I am created by the 2nd year CSE students of DSU using python language.")

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot taken!")

        elif "today news" or "latest news" or 'show news' or "today's news" in query:
            speak("Here are some headlines from the Times of India, Happy reading!")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("https://timesofindia.indiatimes.com/")

        elif 'V S code' in query:
            vsPath = "C:\\Users\\amant\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

        elif 'pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'weather' in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Whats the city name?")
            city_name=takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x['main']
                current_temperature = y['temp']
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n Humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n Humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'battery' in query:
            battery()

        elif 'exit' in query:
            sys.exit(speak("Ok sir, Take Care."))
        
        elif 'music' or 'songs' in query:
            music_direc = 'C:\\Users\\amant\\Downloads\\py project'
            songs = os.listdir(music_direc)
            print(songs)
            os.startfile(os.path.join(music_direc, songs[random.randrange(start=0, stop=1)]))

        elif 'the time' or 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
