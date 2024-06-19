
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
import string
import openai
from openai import OpenAI

class Sarah:
    def __init__(self):
        self.getKey()
        self.assistant()

    def getKey(self):
        
        key_file = open('../../../API.txt')

        key_line = key_file.readline()
        
        key_file.close()
        
        #print(key_line)
        split_line = key_line.split(': ')
        
        #print(split_line[1])

        api_key = split_line[1].rstrip()
        
        return api_key

    def assistant(self):
        #time.sleep(2)
        
        self.respond("How can I help you?")
        
        listening = True
        
        key = self.getKey()
        
        print(key)
        
        self.client = OpenAI(api_key=key)
        
        while listening == True:
            command = self.listen()
            listening = self.responses(command)

    def listen(self, ):
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

    def respond(self, audioString):
        print(audioString)
        
        # Convert to mp3
        tts = gTTS(text=audioString, lang='en')
        tts.save("speech.mp3")
        
        # Play audio file
        playsound(r'speech.mp3')
        
        os.remove('speech.mp3')
        
    def responses(self, command):
        if "hello" in command: 
            listening = True 
            self.respond("Hi")
        elif "what" or "how" or "where" or "when" or "who" or "why" in command:

            listening=True
            
            prompt = [{
                "role" : "user",
                "content" : command
                }]
            
            completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= prompt
            )
        
            response = completion.choices[0].message  
            
        elif "exit" in command: 
            listening = False
            exit(0)
            

        return listening
    
if __name__ == "__main__":
    sarah = Sarah()