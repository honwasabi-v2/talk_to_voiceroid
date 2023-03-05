# -*- coding: utf-8 -*-

OPENAI_SECRET_KEY = "-------APIkey----------------"
OPENAI_ENGINE = 'text-davinci-003'


class api:    
    import openai
    
    def __init__(self, key, engine = OPENAI_ENGINE):
        self.openai.api_key = key
        self.openai_engine = engine
    
    def send(self,prompt):
        print("please wait...(openAIAPI...)")
        completions = self.openai.Completion.create(
            engine= self.openai_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

    
        if completions.choices[0].finish_reason != "stop":
            return -1           
        reply = completions.choices[0].text 
        return reply.split('\n',1)[1]
    
if __name__ == '__main__':
    API = api(OPENAI_SECRET_KEY)
    prompt = input("Enter a prompt: ")
    while(prompt != "EXIT"):
        if prompt != "":
            print(API.send(prompt))
        prompt = input("Enter a prompt: ")
        
        
