# -*- coding: utf-8 -*-
import pyvcroid2
import threading
import time
import winsound
import sys


VOLUME = 1
SPEED = 1
PITCH = 1
EMPHASIS = 1
PAUSE_MIDDLE = 50
PAUSE_LONG = 100
PAUSE_SENTENCE = 200
MASTER_VOLUME = 1

def display_phonetic_label(tts_events):
    start = time.perf_counter()
    now = start
    for item in tts_events:
        tick = item[0] * 0.001
        type = item[1]
        if type != pyvcroid2.TtsEventType.PHONETIC:
            continue
        while (now - start) < tick:
            time.sleep(tick - (now - start))
            now = time.perf_counter()
        value = item[2]
        print(value, end="", flush=True)
    print("")
def get_list():
    with pyvcroid2.VcRoid2() as vc: 
        voice_list = vc.listVoices()
        if 0 < len(voice_list):
            return voice_list
            
        else:
            raise Exception("No voice library")


def speech(message="default",chara = 0):
    with pyvcroid2.VcRoid2() as vc:
        # Load language library
        lang_list = vc.listLanguages()
        try:
            if "standard" in lang_list:
                vc.loadLanguage("standard")
            elif 0 < len(lang_list):
                vc.loadLanguage(lang_list[0])
            else:
                raise Exception("No language library")
        except:       
            print("lang_list = ",lang_list)             
            print(sys.exc_info())
            return 

        
        # Load Voice
        voice_list = vc.listVoices() 
        vc.loadVoice(voice_list[chara])
        
        #print(voice_list[chara])
    
        vc.param.volume = VOLUME
        vc.param.speed = SPEED
        vc.param.pitch = PITCH
        vc.param.emphasis = EMPHASIS
        vc.param.pauseMiddle = PAUSE_MIDDLE
        vc.param.pauseLong = PAUSE_LONG
        vc.param.pauseSentence = PAUSE_SENTENCE
        vc.param.masterVolume = MASTER_VOLUME
    
        # Text to speech
        speech, tts_events = vc.textToSpeech(message)
        
        # Play speech and display phonetic labels simultaneously
        t = threading.Thread(target=display_phonetic_label, args=(tts_events,))
        t.start()
        winsound.PlaySound(speech, winsound.SND_MEMORY)
        t.join()
        
if __name__ == '__main__':
    text = input("text:")
    while text != "EXIT":
        speech(text)
        text = input("text:")
