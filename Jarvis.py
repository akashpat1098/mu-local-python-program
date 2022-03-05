import datetime
import os
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import random


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
def speak(audio):
    '''It takes the audio which computer has to say as string and then it says it'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function when run wish us in audio format according to time'''
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("My name is Jarvis")
    speak("How may i help you")

def takeCommand():
    '''It listen the voice and convert and return it into string  '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\nListening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    '''start the email server'''
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("akashpatel1098@gmail.com","1098akash")
    server.sendmail("akashpatel1098@gmail.com",to,content)
    server.close()
    
if __name__=="__main__":
    emails={"akash":"akashpatel1098@gmail.com","patel":"patelakash1098@gmail.com","sky":"onlyskymovie2020@gmail.com"}
    query="" 
    wishMe()
    webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    chrome=webbrowser.get("chrome")

    while query!= "quit":
    # if 1:
        query=takeCommand().lower()
        name="none" #name is intialised here

        '''these for loop initialise name with a key of dictionary emails if that key is in the   '''
        for key in emails.keys():
            if key in query:
                name=key

# logic for various cammand
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Accoarding to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query: 
            chrome.open("youtube.com")

        elif "open google" in query:
            # webbrowser.open("google.com")
            speak("What should I search on Google")
            cm=takeCommand().lower
            chrome.open(f"{cm}")

        elif "play music" in query:

            music_dir="H:\\87 HONEY SINGH DJ MIX"
            songs=os.listdir(music_dir)
            randSong=random.choice(songs)
            print("Playing Music")
            print(f"Name:{randSong}")
            os.startfile(os.path.join(music_dir,randSong))

        elif f"email to {name}" in query: 
            try:
                speak("What should I say?")
                content=takeCommand()
                to=[emails[email] for email in emails if email in query ]
                speak(f"Email is been sending to {to}")
                print(f"Email is been sending to {to}")
                speak("Please confirm this last time")
                confirmation=takeCommand()
                if confirmation=="yes":
                    sendEmail(to,content)
                    speak("Email has been sent!")
                    print("Email has been sent!")
                else:
                    print("Please try again...")
                    speak("Please try again")
            except Exception as e:
                print(e)
                speak("Sorry,I am unable to send to the mail")