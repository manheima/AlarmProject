#Does things with internal files like list them and play them
import os

#def listFiles
def listSongs():
    songList = os.listdir("/home/pi/Documents/AlarmProject/Songs")
    songList.sort()
    print ""
    for index, song in enumerate(songList):
        print "["+str(index)+"]",song
    print ""

#def playFile
def playSong():
    listSongs()
    songList = os.listdir("/home/pi/Documents/AlarmProject/Songs")
    songList.sort()
    while True:
        songIndex = int(raw_input("Pick a song: "))
        if songIndex < len(songList) and songIndex >= 0:
            break
        else:
            print "Please enter song Index: "
    shellCom = "omxplayer -o local \"/home/pi/Documents/AlarmProject/Songs/"+songList[songIndex]+"\""
    os.system(shellCom)

def playAlarm(songIndex):
    songList = os.listdir("/home/pi/Documents/AlarmProject/Songs")
    songList.sort()
    if songIndex >= len(songList) or songIndex < 0:
        print "Error: Invalid Index"
        return
    shellCom = "lxterminal -e omxplayer -o local \"/home/pi/Documents/AlarmProject/Songs/"+songList[songIndex]+"\""
    os.system(shellCom)

def chooseSong():
    listSongs()
    songList = os.listdir("/home/pi/Documents/AlarmProject/Songs")
    songList.sort()
    while True:
        songIndex = int(raw_input("Pick a song: "))
        if songIndex < len(songList) and songIndex >= 0:
            return str(songIndex)
        else:
            print "Please enter song Index: "

def deleteSong():
    listSongs()
    songList = os.listdir("/home/pi/Documents/AlarmProject/Songs")
    songList.sort()
    while True:
        songIndex = int(raw_input("Pick a song: "))
        if songIndex < len(songList) and songIndex >= 0:
            break
        else:
            print "Please enter song Index to delete: "
    print "Deleting: " + songList[songIndex]
    os.remove("/home/pi/Documents/AlarmProject/Songs/"+songList[songIndex])
