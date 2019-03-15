#import notify2
import speech_recognition as sr
import subprocess
import pyttsx3
import os


if os.path.isfile("config"):
    f = open("config","r").readlines()
    j = []
    configs = {}
    for i in f:
        s = i.split(":")
        configs[str(s[0])]=str(s[1])
else:
    f = open("config","w")
    configs= {}
    configs["music"] = input("Input your music Folder:  ")
    configs["app"] = input("Input app Folder ")
    f.write("music:"+str(configs["music"]))
    f.write("app:"+str(configs["app"]))

engine = pyttsx3.init();


r = sr.Recognizer()
mic = sr.Microphone()
#notify2.init('Nathan')
while True:
    with mic as source:
        print("Adjusting")
        r.adjust_for_ambient_noise(source)
        print("Listening")
        audio=r.listen(source)
        print("Recognizing")
        s=r.recognize_google(audio)
        print(s)
        if True:
            if "open" in s.lower() or "run" in s.lower():
                from modules.run_app import find_app
                from nlp_utils.nlp import treat
                to_open = treat(s.lower(), "open")
                find_app(to_open, configs["app"])
                engine.say("I will do it sir.");
                engine.runAndWait();
            if "play" in s.lower():
                from modules.play_music import find_music
                from nlp_utils.nlp import treat
                to_open = treat(s.lower(), "play")
                find_music(to_open, configs["music"])
                engine.say("I will do it sir.");
                engine.runAndWait();