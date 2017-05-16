#Search For a youtube video
import webbrowser
import urllib2
from bs4 import BeautifulSoup
import os
import glob

def songSearch():
    textToSearch = str(raw_input("Search Youtube for: "))
    print "Please wait this takes a minute..."
    query = textToSearch.replace(" ","+")
    url = "https://www.youtube.com/results?search_query=" + query

    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if vid['href'][0:6] == "/watch":
            downloadURL = 'https://www.youtube.com' + vid['href']
            return downloadURL
            break

#Now Download this music to songs folder
def downloadUrl(downloadURL):
    shellCommand = "youtube-dl -w -f best -o " + "\"/home/pi/Documents/AlarmProject/Songs/%(title)s-%(id)s.%(ext)s\" " + downloadURL
    print "Video Found!"
    print "Downloading: " + downloadURL
    os.system(shellCommand)
    #Now check if download is webm
    if lastFile()[-3:] != 'mp4':
        print "File is old format so downloading audio only..."
        #delete the file then download a webm version
        os.remove(lastFile())
        downloadWebm(downloadURL)

        
def downloadWebm(downloadURL):
    shellCommand = "youtube-dl --extract-audio -o " + "\"/home/pi/Documents/AlarmProject/Songs/%(title)s-%(id)s.%(ext)s\" " + downloadURL
    print "Video Found!"
    print "Downloading: " + downloadURL
    os.system(shellCommand)

def lastFile():
    path = '/home/pi/Documents/AlarmProject/Songs/*'
    list_of_files = glob.glob(path)
    latest_file = max(list_of_files, key = os.path.getctime)
    return latest_file    

