#Plays alarm
import songFiles
import sys

#Somehow figure out which alarm you are and play the corresponding song
def main():
    songIndex = int(sys.argv[1])
    songFiles.playAlarm(songIndex)    


#-----------------------------Start main at end----------------------------
#Start program after compiler knows all our functions        
if __name__ == '__main__':
    main()
