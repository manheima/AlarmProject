#WakeUp to a song on youtube Script
import webbrowser
import numpy as np

musicLib = {
    0: 'https://www.youtube.com/watch?v=JGhoLcsr8GA',
    1: 'https://www.youtube.com/watch?v=IcrbM1l_BoIs',
    2: 'https://www.youtube.com/watch?v=zaGUr6wzyT8'
}

randSong = np.random.randint(1,len(musicLib)) 
webbrowser.open(musicLib[randSong])
