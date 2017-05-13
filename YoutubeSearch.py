#Search For a youtube video
import webbrowser
import urllib2
from bs4 import BeautifulSoup
import os

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
    shellCommand = "youtube-dl -w -f best -o " + "\"/home/pi/Documents/Alarm Project/Songs/%(title)s-%(id)s.%(ext)s\" " + downloadURL
    print "Video Found!"
    print "Downloading: " + downloadURL
    os.system(shellCommand)


