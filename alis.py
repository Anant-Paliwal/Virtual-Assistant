import ctypes
import datetime
# import winshell
import json
import math
import operator
import os
import random
import shutil
import smtplib
import subprocess
import sys
import time
import tkinter
from urllib.parse import urldefrag
import webbrowser
from audioop import mul
from urllib.request import urlopen

# import feedparser
# # import matplotlib.pyplot as plt
# # import numpy as np
import pandas as pd
import pyaudio
import pyjokes
import pyttsx3
import pywhatkit as kit
# import requests
import speech_recognition as sr
import wikipedia
import win32com.client as wincl
import wolframalpha
from bs4 import BeautifulSoup
# from clint.textui import progress
from pywhatkit.sc import shutdown
from twilio.rest import Client

# # from ecapture import ecapture as ec

# import weather_forecast



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

def wishme():
    hour = int( datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Everning!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        
        r.pause_threshold=1
        audio = r.listen(source)
     

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"user said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "none"
        return query

         
def  sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',507)
    server.ehlo()
    server.starttls()
    server.login('anant31122000@gmail.com','password')
    server.sendmail('anant31122000@gmail.com',to,content)
    server.close()

def read():
    data=pd.read_csv("tips.csv")
    data.head()
    
    

if __name__ == "__main__":
    
  wishme()
#   speak("Hi sir i am alis")
  speak("Hi sir i am alis")
    
  speak("How can i help you ")
  while True:
        

     query = takecommand().lower()

    #Logic Task

    #  if 'alis' in query:
    #       print(query)    
   
     if 'wikipedia' in query:
        speak('Searching wikipedia')
        query=query.replace('wikipedia', "")
        results=wikipedia.summary(query, sentences=2)
        speak('accourding ti wikipedia...')
        print(results)
        speak(results)
     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
     elif 'open google' in query:
        webbrowser.open("google.com")
     elif 'open Email' in query:
        webbrowser.open("mail.google.com")
        
     elif 'what is your name' in query:
        print('alis')
        speak("alis ")
     elif 'play music' in query:
        
        path="E:\\latest songs\\"
        files=os.listdir(path)
        d=random.choice(files)
        
        os.startfile('E:\\latest songs\\'+d)
     elif 'open Notepad' in query:
        
        path="%windir%\\system32\\notepad.exe"
        files=os.listdir(path)
        
        
        os.startfile('%windir%\\system32\\notepad.exe'+files)
        
     elif 'time' in query:  
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f'The time is :{strTime}')

     elif 'send email' in query:
        try:
            speak("What should i say?")
            content = takecommand()
            to="anant31122000@gmail.com"
            sendEmail(to,content)
            speak("Email has been send")
        except Exception as e:
            print(e)
            speak("Sorry I can not send email it's some issue")    

     elif 'exist' in query:
        break
        speak('Thanks sir')
     elif 'play video' in query or 'play movie' in query:
         song = query.replace('play video','')
         song = query.replace('play movie','')
         speak('Playing'+song)
         kit.playonyt(song)
     elif 'jokes' in query:
         speak(pyjokes.get_joke())
     elif "will you be my gf" in query or "will you be my bf" in query:  
         speak("I'm not sure about, may be you should give me some time")
         
    
     elif 'send message' in query:
         kit.sendwhatmsg('+918191017502','hi i am alis',18,57)
     
     elif 'search' in query:
         search = query.replace('search','')
         speak('searching'+search)
         print(search)
         kit.search(search)
     
     elif 'shutdown computer' in query:
         shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
         if shutdown == 'no':
             speak('ok sir')
             exit()
         else:    

           print(query)
         speak('shutdown system')
         os.system('shutdown /s /t 1')
     elif 'restart computer' in query:
         speak('restart system')
         os.system('shutdown /r ') 
     elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

    #  elif 'empty recycle bin' in query:
    #         winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    #         speak("Recycle Bin Recycled")
 
     elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop alis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
 
     elif "locate me" in query or "Locate my location" in query:
            query = query.replace("where is", "")
            query = query.replace("Locate my location", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/@26.7812531,79.0290167,16z?hl=en" + location + "")
 
    #  elif "camera" in query or "take a photo" in query:
    #         ec.capture(0, "alis Camera ", "img.jpg")

     elif "calculate" in query.lower():
             
          app_id = "JXYYEY-WP2XA7U6AQ" 
          client = wolframalpha.Client(app_id)
  
          indx = input.lower().split().index('calculate')
          query = input.split()[indx + 1:]
          res = client.query(' '.join(query))
          answer = next(res.results).text
          print(answer)
          speak("The answer is " + answer)
            
        #Ask question
     
     
     elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
    #  elif  'tell me about manu future' in query:
    #         speak('sir,your brother future is useless')  
     elif 'tell me your creators  future' in query:
            speak('sir your future is bright')            
     
     elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")    
     elif "who made you" in query or "who created you" in query:
            speak("I have been created by Anant Paliwal.")
     elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
     elif 'where you live' in query:
           speak('i am live in cloud') 

     elif 'can you help me in study' in query :
           speak('In which subject sir ')

        #    python course
     elif 'python' in query:
          speak('it is very popular language that time')
     elif 'tell me about if else' in query or 'what is if else' in query:
          speak('if else are use to give a condition like a true and false')

        # Perday normal talk
     elif 'what are you doing ' in query:
           speak('waiting for your command sir')   
     elif 'do free talk like a friend ' in query:
           speak( 'ok anant' )
     elif 'deva i am not feel well ' in query:
          speak('why sir')
     elif  'life is boring' in query:
         speak( 'ohh sir can i play music for fresh mood')
     elif  'sir can i call your mom ' in query or 'call mom ' in query:
         speak('ok sir...')                               
     elif 'i love you' in query:
            speak('I love you to')  
     elif  'do you love me' in query:
            speak('Yes i can also you')
     elif  'do you marry me' in query:
            speak('Yes it my pleasure but i am machine it is so sad for me ')
                         
 
     elif "who are you" in query:
            speak("I am your virtual assistant created by Anant ")
 
     elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Anant")
 
     elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:\\Users\\paliwal\\OneDrive\\Desktop\\window 11\\11.jpg",
                                                       0)
            speak("Background changed successfully")
     elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
     elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

 
     elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('E:\\jarvis\\alis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
     elif "show note" in query:
            speak("Showing Notes")
            file = open("E:\\jarvis\\alis.txt", "r")
            print(file.read())
            speak(file.read(6))
     

             
     elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takecommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)

    #  elif 'weather' in query:
    #     speak('Today weather')
    #     weather_forecast.forecast(query)
    #     speak(query)
    #     print(query)           
        
      

     elif 'addition'in query or 'sum' in query or 'add' in query:
       try:  

        a=int( takecommand())
        speak("+")
        b=int(takecommand())
        
        # print(type(a))
        sum=operator.add(a,b)
        print("The sum is :",sum)
        speak(sum)  

       except Exception as e:
           print(e)
           print("Sorry sir there is some problem")   

        #Subtraction 
     elif 'subtraction'in query or 'subtract' in query:
       try:  

        a=int( takecommand())
        speak("-")
        b=int(takecommand())
        
        # print(type(a))
        c=operator.sub(a,b)
        print("The Subtraction is :",c);    
        speak(c)

       except Exception as e:
           print(e)
           print("Sorry sir there is some problem")   
 
        # Multiplication
     elif 'multiplication'in query or 'multiply' in query:
         
       try:  
        a=int( takecommand())
        speak("*")
        b=int(takecommand())
        
        # print(type(a))
        c=operator.mul(a,b)
        print("The Multipication is :",c);  
        speak(c)  
       except Exception as e:
           print(e)
           print("Sorry sir there is some problem")   
            
        # Division
     elif 'division'in query or 'divide' in query:
         
       try:  
        a=int( takecommand())
        speak("/")
        b=int(takecommand())
        
        # print(type(a))
        c=operator.floordiv(a,b)
        print("The Division is :",c);   
        speak(c) 
       except Exception as e:
           print(e)
           print("Sorry sir there is some problem")  

     elif 'power'in query or 'square' in query:
       try:  

        a=int( takecommand())
        speak("square")
        b=int(2)
        
        # print(type(a))
        power=operator.pow(a,b)
        print("The Power is :",power)
        speak(power)  

       except Exception as e:
           print(e)
           print("Sorry sir there is some problem")   
    
         #   Data Science Command

    #  elif  ' read data' in query:
    #      data=pd.read_csv('tips.csv')
    #     #  data.head()
    #      print(data.head())
    #      speak("This is your shortest data")
 

     elif 'exit' in query:
         speak('Thankyou sir have a good day')
         
         sys.exit()

     elif  'no' in query :
          speak('so how can i help sir')
     else :
           path="E:\\latest songs\\"
           files=os.listdir(path)
           d=random.choice(files)
        
           os.startfile('E:\\latest songs\\'+d)
           speak('')   

        

