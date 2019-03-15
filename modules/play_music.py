import subprocess
import os
from Levenshtein import distance
import fnmatch

def find_music(app, root):
    tolaunch=""
    minimum=999999
    path = root
    papth = os.walk(path)
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(root, filename)
            r=int(distance(filename, app))
            #print("app : "+str(name)+" distance : "+str(r))
            if r<minimum:
                tolaunch=filePath
                minimum=r
                print("actual best : "+str(tolaunch)+ " distance : "+str(minimum))
    os.system("open \""+tolaunch+"\"")

