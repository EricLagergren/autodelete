import os
import sys
import sh
from datetime import datetime, time, date, timedelta

sys.stdout = open('/var/log/autodelete.log', 'a')
file_name = '/var/log/autodelete.log'

def checkLog():
	if (os.path.isfile(file_name) == True):
		print("Ok, this file's here!")
	else:
		open('/var/log/autodelete.log', 'w+')
checkLog()

path = "/path/to/folder" # EDIT THIS VARIABLE FOR THE FOLDER YOU WANNA DELETE FILES FROM !!!!!!!!!!!!!!!!!

def cleanDir(dir):
    for file in os.listdir(dir):
        fullpath = os.path.join(dir, file)
        mdate = datetime.fromtimestamp(os.path.getmtime(fullpath))
        now = datetime.now()
        if (now - mdate) > timedelta(seconds=5):
            if os.path.isfile(fullpath):
                os.remove(fullpath)
            elif os.path.isdir(fullpath):
                cleanDir(fullpath)
cleanDir(path)

def writeToLog():
	if cleanDir(path) == False:
		print("Shit done fucked up" + " " + datetime.now().strftime("%m-%d-%y"))
	else:
		print("All good, captain" + " " + datetime.now().strftime("%m-%d-%y"))
writeToLog()
