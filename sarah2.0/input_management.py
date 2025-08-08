import speech_recognition as sr

import output_management


class command_input:
    def __init__(self):

        # Set input mode flag; 0=console/text, 1=audio
        self.input_mode = 0

        self.greeting = "How can I help you?\n"

        self.command = ""



    def run_input(self):
        #time.sleep(2)

        # Check for text vs audio input mode
        if self.input_mode == 1:
            self.get_audio_input()      

        else:
            self.get_text_input()

        return self.command



    def get_text_input(self):

        # Get user input
        self.command = input(self.greeting)


    def get_audio_input(self):
        output_management.speak(self.greeting)
        
        listening = True
        
        while listening == True:
            self.command = listen()
            listening = responses(self.command)



    def listen(self):
        
        # Instantiate SpeechRecognizer 
        rec = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening for self.command...")
            audio = rec.listen(source)
            self.command = ""

        try:
            print("trying to dc self.command")
            self.command = rec.recognize_google(audio)
            print("self.command given: ", self.command)
            
        except sr.UnknownValueError:
            print("Audio was not understandable")
            
        except sr.RequestError as e:
            print("Request failed: ".format(e))


    # Getter methods- currently not needed
    def get_command(self):
        return self.command

    def get_input_type(self):
        return self.input_mode 