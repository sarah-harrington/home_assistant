
from socketserver import ThreadingUDPServer
import pyaudio
import speech_recognition as speerec
import time
import os
from gtts import gTTS
import requests, json
from playsound import playsound
from googlesearch import search
import pandas as pd
from serpapi import GoogleSearch
import openai

def assistant():
    #time.sleep(2)
    
    respond("How can I help you?")
    
    listening = True
    
    while listening == True:
        command = listen()
        listening = responses(command)

def listen():
    rec = speerec.Recognizer()
    
    with speerec.Microphone() as source:
        print("Listening for command...")
        audio = rec.listen(source)
        command = ""

    try:
        command = rec.recognize_google(audio)
        print("Command given: ", command)
        
    except speerec.UnknownValueError:
        print("Audio was not understandable")
        
    except speerec.RequestError as e:
        print("Request failed: ".format(e))
        

    return command

def respond(audioString):
    print(audioString)
    
    # Convert to mp3
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    
    # Play audio file
    playsound(r'speech.mp3')
    
    os.remove('speech.mp3')
    
def responses(command):
    if "hello" in command: 
        listening = True 
        respond("Hi")
    elif "what" or "how" or "where" or "when" or "who" or "why" in command:
        listening=True
        
        
        
        client = openai.OpenAI()
        
        prompt = [{
            "role" : "user",
            "content" : command
            }]
        
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=prompt)
        
        reply = chat.choices[0].message.content
        response = reply

        #geo_json = json.loads(geo_req.text)
        '''
        search = GoogleSearch({
            'q' : command,
            'location' : geo_json['city']
            
            })
          '''  
        
    elif "exit" in command: 
        listening = False
        exit()
        

    return listening
     
assistant()