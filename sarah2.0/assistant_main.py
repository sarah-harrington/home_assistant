class assistant:

    def __init__(self, model, query):
         self.model = "gpt-3.5-turbo"


    def responses(command):
            
            if "hello" in command: 
                listening = True 
                respond("Hi")
            elif "what" or "how" or "where" or "when" or "who" or "why" in command:
                listening=True
                
                prompt = [{
                    "role" : "user",
                    "content" : command
                    }]
                
                chat = openai.chat.completions.create(model= self.model, messages=prompt)
                
                reply = chat.choices[0].message.content
                response = reply
                
            elif "exit" in command: 
                listening = False
                exit()
                

            return listening