#######################################################################################################################
# This application is written for a Linux OS
#######################################################################################################################


import datetime
import os
import smtplib
import pyautogui
import speech_recognition as sr
import wikipedia
from screenrecorder import screenrecorder
from face_detector import facedetection
from addpoint import *

engine = pyttsx3.init()

aaron = 'askinner@ornerylion.com'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 145)


def screenshot():
    img = pyautogui.screenshot()
    img.save('/home/aaron/Desktop/ss.png')


def who_am_i():
    speak(
        "I am K.A.S version 1.1 or Kas... short for Keeping Aaron Sane, i am a program written by aaron to help keep "
        "himself together")


def time():
    current_time = datetime.datetime.now().strftime("%I:%M")
    speak('the time is ')
    speak(current_time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    today_date = int(datetime.datetime.now().day)
    speak(month)
    speak(today_date)
    speak(year)


def system_monitor():
    speak('booting system monitor now')
    os.system('conky -c /home/aaron/.config/conky/conky.conf')
    engine.runAndWait()


def system_monitor_shutdown():
    speak('closing system monitor')
    os.system('pkill conky')


def greeting():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good afternoon sir")
    elif 18 <= hour < 24:
        speak("Good Evening Sir")
    speak("welcome back")

    speak('today is')
    date()

    time()


def spotify():
    pass


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aaroncurtisskinner@gmail.com', 'P@int0909')
    server.sendmail('aaroncurtisskinner@gmail.com', to, content)
    server.close()


def voicecommand():
    rec = sr.Recognizer()
    with sr.Microphone() as audio_source:
        print('Listening...')
        rec.pause_threshold = 1
        audio = rec.listen(audio_source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='english')
        print(query)

    except Exception as e:
        print(e)
        speak("can you say that again")

        return "None"
    if 'date' in query:
        date()

    if "start system monitor" in query:
        system_monitor()

    elif query == 'stop system monitor':
        system_monitor_shutdown()

    elif 'record screen' in query:
        screenrecorder()

    elif query == 'who are you':
        who_am_i()

    elif query == 'I have another question':
        voicecommand()
    elif 'screenshot' in query:
        screenshot()
        speak('screenshot captured')
    elif 'open Spotify' in query:
        spotify()

    elif "Wikipedia" in query:

        speak("I am Searching...")
        query = query.replace("wikipedia", "")
        wikipedia.search(query)
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)

    elif 'send email' in query:
        try:
            speak('What would you like to send')
            content = voicecommand()
            engine.runAndWait()
            speak('Who should i send this to')
            to = input('enter email address')
            speak('sending email')
            send_email(to, content)

        except Exception as e:
            print(e)
            speak('unable to send email')

    elif 'log out' in query:
        os.system('gnome-session-quit')

    elif 'start face recognition' or 'start facial recognition' in query:
        facedetection()
    elif 'shut down' in query:
        os.system('shutdown')

    elif 'restart' in query:
        os.system('shutdown -r now')

    elif 'add point for Jack' in query:
        pass
    elif 'subtract point for Jack' in query:
        pass

    elif 'add point for fin' in query:
        pass

    elif query == 'subtract point for fin' or 'subtract .4 fin':
        pass


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            voicecommand()
