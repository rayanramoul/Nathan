import os
from sound_utils import *

def process(path):
    outputs={}
    inputs={}
    pre_output=[]
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(".txt"):
                pre_output.append(os.path.join(dirpath, file))
            else:
                inputs[os.path.splitext(file)[0]] = os.path.join(dirpath, file)

    for i in pre_output:
        fix = open(i, "r")
        lines = fix.readlines()
        for j in lines:
            lix = j.split(" ")
            outputs[lix[0]]=[]
            outputs[lix[0]]= lix[1:]

    print("4362-15663-0085 : ")
    print("Input : "+str(inputs['4362-15663-0085']))
    print("Output : "+str(outputs['4362-15663-0085']))

process("./Audios")
    