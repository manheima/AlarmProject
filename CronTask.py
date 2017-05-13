#schedule tasks in crontab using python

import os

#path = "/etc/cron.d"
path = "/home/pi/Documents/Alarm Project"
with open(path+"/aaron_task.txt","a") as myfile:
	#myfile.write("13 11 * * * /bin/sh \"/home/pi/Documents/Alarm Project/job.sh\" \n")
        myfile.write("17 44 * * * \"/home/pi/Documents/Alarm Project/job.sh\" \n")

print "cron file written"

