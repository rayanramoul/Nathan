import subprocess
import os
from Levenshtein import distance


def find_app(app, root):
    print("Trying to run : "+str(app))
    tolaunch=""
    minimum=999999
    path = root
    files = os.listdir(path)
    for name in files:
        r=int(distance(name, app))
        #print("app : "+str(name)+" distance : "+str(r))
        if r<minimum:
            tolaunch=name
            minimum=r
            print("actual best : "+str(tolaunch)+ " distance : "+str(minimum))
    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/"+tolaunch])