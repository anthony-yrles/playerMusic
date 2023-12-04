def playSong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(f'./songs/{currentsong}')
    mixer.music.play()

def pauseSong():
    mixer.music.pause()

def stopSong():
    mixer.music.stop()

def resumeSong():
    mixer.music.unpause()

def volumeDown():
    global volume
    volume = volume - 0.1
    if volume  < 0:
        volume = 0
    print(volume)
    mixer.music.set_volume(volume)

    
def volumeUp():
    global volume
    volume = volume + 0.1
    if volume > 1:
        volume = 1
    print(volume)
    mixer.music.set_volume(volume)

def songsLoop():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(f'./songs/{currentsong}')
    mixer.music.play(-1)