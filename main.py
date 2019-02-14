'''
import sounddevice as sd
import numpy as np

duration = 5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    outdata[:] = indata# output 
    print(len(outdata))
with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))
'''

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Adjusting")
    r.adjust_for_ambient_noise(source)
    print("Listening")
    audio=r.listen(source)
    print("Type "+str(type(audio)))
#    print("Len "+str(len(audio)))
    print("Audio : "+str(audio))
    print("Recognizing")
    print(r.recognize_sphinx(audio))