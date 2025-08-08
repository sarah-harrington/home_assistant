import pyaudio

import time
import os
from gtts import gTTS
import requests, json
from playsound import playsound
from googlesearch import search
import pandas as pd
from serpapi import GoogleSearch
import openai

import input_management



def main():
    
    print(f"Starting SARAH...\n")

    # Get input
    input_obj = input_management.command_input()
    command_given = input_obj.run_input()

    print("Command given: ", command_given)


if __name__ == "__main__":
    main()

    

