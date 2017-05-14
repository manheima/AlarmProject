#create a menu to set up an alarm
import os
import YoutubeSearch #i made this
import songFiles #i made this one too
from shutil import copyfile #copyfile(src,dst)

#-----------constant variables---------------
ALARM_DIC = {'0':"Sunday",
            '1':"Monday",
            '2':"Tuesday",
            '3':"Wednesday",
            '4':"Thursday",
            '5':"Friday",
            '6':"Saturday",
            '*':"Everyday"}
            

#------------------------Main---------------------------------
def main():
    menu = {};
    menu['1'] = "Edit Alarms"
    menu['2'] = "Alarm Songs"
    menu['3'] = "Set Volume"
    menu['4'] = "Exit"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '[' + entry + ']', menu[entry]
        selection = raw_input("Please Select: ")
        if selection == '1':
            editAlarms()
        elif selection == '2':
            viewSongs()
        elif selection == '4':
            break
        elif selection == '3':
            setVolume()
        else:
            print "Unknown Option Selected: "
        #Now just skip a line
        print ""
        
#---------------------------Functions----------------------------------
def editAlarms():
    print " "
    menu = {};
    menu['1'] = "Add an alarm"
    menu['2'] = "Delete an alarm"
    menu['3'] = "View Alarms"
    menu['4'] = "Exit"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '[' + entry + ']', menu[entry]
        selection = raw_input("Please Select: ")
        if selection == '1':
            addAlarm()
        elif selection == '2':
            deleteAlarm()
        elif selection == '3':
            viewAlarms()
        elif selection == '4':
            break
        else:
            print "Unknown Option Selected: "
        #Now just skip a line
        print ""

def viewAlarms():
    print " "
    #os.system("crontab -l")
    with open('/home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt', 'r') as f:
        count = 0
        for line in f:
            if count%3 ==0:
                print "["+str(count/3)+"] " +line[0:-1]
            count+=1
    

def addAlarm():
    newAlarm = Alarm()
    #add user input before this to get hour, min ,etc
    print ""
    print "Enter Time in [hh:mm]. For example, 8:30"
    time = raw_input("Enter Time: ")
    while ':' not in time:
        "Invalid Format. Please use: [hh:mm]. For example 8:30"
        time = raw_input("Enter Time: ")
    newAlarm.hour = str(int(time[0:time.index(':')]))
    newAlarm.minute = str(int(time[time.index(':')+1:len(time)]))
    print "Alarm set for "+newAlarm.hour+":" + newAlarm.minute
    #get day(s) of week to set alarm
    print ""
    print "Enter Day(s) of week (separated by commas if multiple)"
    print "where 0 = Sun, 1 = Mon, 2 = Tues, 3 = Weds, 4 = Thurs, 5 = Fri, 6 = Sat" 
    validChars = set(['0','1','2','3','4','5','6','-',',', ' '])
    days = raw_input("Enter Day(s) of week:")
    if days!='':
        daysSet = set(days)
        while (daysSet.intersection(validChars) != daysSet) or (days[-1] == ','):
            print "Invalid entry. Try again:"
            days = raw_input("Enter Day(s) of week:")
            daysSet = set(days)
    if days!="":
        newAlarm.dow = days
    #get song to set
    print " "
    newAlarm.song = songFiles.chooseSong()
    
    newAlarm.setAlarm()

def setVolume():
    volume = -1
    while volume > 100 or volume <0:
        try:
            volume = int(raw_input("Set Alarm Volume (0-100): "))
        except ValueError:
            print "Invalid Entry"
    shellCommand = "amixer set PCM " + str(volume)
    os.system(shellCommand)
    

def addAlarmSong():
    print ""
    menu = {};
    menu['1'] = "Enter Youtube URL Directly"
    menu['2'] = "Put in search term"
    menu['3'] = "Return to previous menu"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '[' + entry + ']', menu[entry]
        selection = raw_input("Please Select: ")
        if selection == '1':
            YoutubeSearch.downloadUrl(str(raw_input("Enter URL: ")))
        elif selection == '2':
            YoutubeSearch.downloadUrl(YoutubeSearch.songSearch())
        elif selection == '3':
            break
        else:
            print "Unknown option selected"

def deleteAlarm():
    print ""
    menu = {};
    menu['1'] = "Delete All Alarms"
    menu['2'] = "Delete a specific alarm"
    menu['3'] = "Return to previous menu"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '[' + entry + ']', menu[entry]
        selection = raw_input("Please Select: ")
        if selection == '1':
            deleteAllAlarms()
        elif selection == '2':
            deleteSpecificAlarm()
        elif selection == '3':
            break
        else:
            print "Unknown option selected"

def deleteSpecificAlarm():
    viewAlarms()
    print "viewAlarms"
    indexToDelete = int(raw_input("Please select index of alarm to delete: "))
    #open the file, read it, delete the specific lines, write it back in
    f = open('/home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('/home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt', 'w')
    for lineIndex,line in enumerate(lines):
        if (lineIndex != indexToDelete*3) and (lineIndex != (indexToDelete*3+1)) and (lineIndex != (indexToDelete*3+2)):
            f.write(line)
    f.close()
    #then write txt file to cron
    writeToCrontab()
    print "Alarm deleted"



def deleteAllAlarms():
    open('/home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt', 'w').close()
    writeToCrontab()
    print "All alarms deleted"
    print ""

def viewSongs():
    print ""
    menu = {};
    menu['1'] = "Add a new song"
    menu['2'] = "List songs"
    menu['3'] = "Play a song"
    menu['4'] = "Delete a song"
    menu['5'] = "Return to previous menu"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '[' + entry + ']', menu[entry]
        selection = raw_input("Please Select: ")
        if selection == '1':
            addAlarmSong()
        elif selection == '2':
            songFiles.listSongs()
        elif selection == '3':
            songFiles.playSong()
        elif selection == '4':
            songFiles.deleteSong()
        elif selection == '5':
            break
        else:
            print "Unknown option selected"

def clearScreen():
    os.system("clear")

#-----------------------------Classes-------------------------------

#Define an alarm class
class Alarm:
    def __init__(self, minute='*', hour='*', dom='*', month='*', dow='*', song = 0):
        self.minute = str(minute)
        self.hour = str(hour)
        self.dom = str(dom)
        self.month = str(month)
        self.dow = str(dow)
        self.song = str(song)
    def setAlarm(self):
        #first write the alarm info as a comment in txt file
        dowString = ""
        for key in self.dow:
            if (key==',') or (key=='-'):
                dowString = dowString + key + " "
            else:
                dowString = dowString + ALARM_DIC[key] + " "
        alarmComment = "#Alarm set for "+self.hour+':'+self.minute+" on "+ dowString
        print alarmComment
        writeToFile(alarmComment)
        
        #write the crontab command to a local file
        crontabString = self.minute +" "+ self.hour +" "+ self.dom +" "+ self.month +" "+ self.dow
        crontabCommand = ' /home/pi/Documents/AlarmProject/AlarmFiles/myCronJob.sh' + ' '+ self.song
        writeToFile(crontabString+crontabCommand+'\n')
        #now write that file to crontab
        writeToCrontab()
            
#Helper functions for alarm class
def writeToFile(stringToWrite, path = '/home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt', action='a'):
    with open(path,action) as myfile:
        myfile.write(stringToWrite+'\n')

def writeToCrontab():
    shellCommand = "crontab /home/pi/Documents/AlarmProject/AlarmFiles/myCron.txt" 
    os.system(shellCommand)
    


#-----------------------------Start main at end----------------------------
#Start program after compiler knows all our functions        
if __name__ == '__main__':
    main()


#--------------------Notes to Self---------------------------------
##    #to download music to songs folder use linux command:
##    youtube-dl -w -o "/home/pi/Documents/Alarm Project/Songs/%(title)s-%(id)s.%(ext)s" https://www.youtube.com/watch?v=IcrbM1l_BoIs

##    
##    #to play music use linux command:
##    omxplayer -o local Downtown.webm
##    omxplayer -o local /home/pi/Documents/Alarm\ Project/Songs/WakeMeUp.mp4

    
    
