# -*- coding: utf-8 -*
"""
Created on Thu Oct 27 16:22:36 2022

@author: honwasabi

"""



import sys
import speech_to_text as stt
import text_to_speech as tts

G_CHARA = 0
G_API = None


class talk_message:
    CHARA = 0
    def __init__(self,chara = 0):
            self.CHARA = chara;
    def set_chara(self,num):
        self.CHARA = num
    
    def input_message(self,api):
        while(1):
            message = input("message : ")
            if message in command.COMMAND:
                command.COMMAND[message](command)
            reply  = api.send(message)
            print(reply)
            tts.speech(reply,self.CHARA)
            
    def input_speech(self,api):
        while(1):
            stt.recording()
            message = stt.wav_to_text()  
            print(message)
            if message in command.COMMAND:
                command.COMMAND[message](command)
            reply  = api.send(message)
            print(reply)
            tts.speech(reply,self.CHARA)


#特殊入力処理
class command:
    def command_exit(self) :
        print("exit")
        sys.exit()
    
    def command_err(self):
        print("please input message")
        message = input("message : ")
        if message in self.COMMAND:
            self.COMMAND[message](self)    
    
    def command_openai(self):
        import openaiAPI as API
        global G_API
        key = input("openAI_APIkey:")
        G_API = API.api(key)
        tm = talk_message(G_CHARA)
        tm.input_message(G_API)

    
    def command_talkapi(self):
        import talkAPI as API
        global G_API        
        key = input("talkAPI_APIkey:")
        G_API = API.api(key)
        tm = talk_message(G_CHARA)
        tm.input_message(G_API)
        
    def command_list(self):
        for command in self.COMMAND:
            print(command)
        message = input("message : ")
        if message in self.COMMAND:
            self.COMMAND[message](self)  
            
    def command_say(self):
        print("音声入力モード")
        tm = talk_message(G_CHARA)
        tm.input_speech(G_API)
            
    def command_keybord(self):
        print("キーボード入力モード")
        tm = talk_message(G_CHARA)
        tm.input_message(G_API)
    
    def command_chara(self):    
        global G_CHARA 
        voiceroid_list = tts.get_list()
        for i,name in enumerate(voiceroid_list):
            print(i,name)
        while 1:
            try:
                chara = int(input("会話するキャラの番号を入力してください"))
                if 0 <= chara <= len(voiceroid_list)-1 :
                    G_CHARA = chara
                    tm = talk_message(G_CHARA)
                    break
                else:
                    print("0から",len(voiceroid_list)-1,"までの数字を入力してください")
            except ValueError:
                print ("エラー：数字以外の文字を入力しないでください。")
        tm.input_message(G_API)
            
            
    COMMAND = {"-EXIT":command_exit,              
               "-q":command_exit,
               "-openAIAPI":command_openai,
               "-talkAPI":command_talkapi,
               "-help":command_list,
               "-h":command_list,
               "-list":command_list,
               "-say":command_say,
               "-chara":command_chara,
               "": command_err,
               "終了":command_exit,
               "キーボード":command_keybord,               
               }
    
if __name__ == "__main__":
    voiceroid_list = tts.get_list()
    for i,name in enumerate(voiceroid_list):
        print(i,name)
    chara = 0
    while 1:
        try:
            chara = int(input("会話するキャラの番号を入力してください"))
            if 0 <= chara <= len(voiceroid_list)-1 :
                G_CHARA = chara
                tm = talk_message(G_CHARA)
                break
            else:
                print("0から",len(voiceroid_list)-1,"までの数字を入力してください")
        except ValueError:
            print ("エラー：数字以外の文字を入力しないでください。")
    
      
    while(1):
        num_API = input("0:TalkAPI\n1:openAIAPI\nAPI?:")
        if(num_API == "0"):
            import talkAPI as API
            key = input("talkAPI_APIkey:")
            G_API = API.api(key)
            tm.input_speech(G_API)
        elif(num_API == "1"):
            import openaiAPI as API
            key = input("openAI_APIkey:")
            G_API = API.api(key)
            tm.input_speech(G_API)
            


    
    

        



