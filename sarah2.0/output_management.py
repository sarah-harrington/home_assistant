

def speak(audioString):
    print(audioString)
    
    # Convert to mp3
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    
    # Play audio file
    playsound(r'speech.mp3')
    
    os.remove('speech.mp3')