import os
from sound_utils import *
from nltk import word_tokenize

def process(path):
    outputs={}
    inputs={}
    pre_output=[]
    x=0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(".txt"):
                pre_output.append(os.path.join(dirpath, file))
            elif file.endswith(".flac"):
                inputs[os.path.splitext(file)[0]] = transform_mfcc(os.path.join(dirpath, file))

    for i in pre_output:
        fix = open(i, "r")
        lines = fix.readlines()
        for j in lines:
            lix = j.split(" ")
            outputs[lix[0]]=[]
            outputs[lix[0]]= (" ".join(word_tokenize(" ".join(lix[1:])))).split(" ")
            print("output : "+str(outputs[lix[0]]))
    total_mean=0
    count=0
    for j in inputs:
        print("Relation : "+str(len(inputs[j])/len(outputs[j])))
        total_mean += len(inputs[j])/len(outputs[j])
        count+=1
       
    return (inputs, outputs)
    
process()
    