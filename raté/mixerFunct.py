from pygame import mixer
from tkinter import *

pause = False
volume = 0.5

def playSong(song):
    mixer.music.load(f'./songs/{song}')
    mixer.music.play()

def pauseSong():
    global pause

    if not pause:
        mixer.music.pause()
        pause = True
    else:
        mixer.music.unpause()
        pause = False

def stopSong():
    mixer.music.stop()

def resumeSong():
    mixer.music.unpause()

def volumeDown(canvas):
    global volume
    volume = volume - 0.1
    scaleVolume = volume * 200
    if volume  < 0:
        volume = 0
    mixer.music.set_volume(volume)
    canvas.delete("volume_bar")
    canvas.create_rectangle(100, 50, 100 + scaleVolume, 80, fill='red', tags="volume_bar")

    
def volumeUp(canvas):
    global volume
    volume = volume + 0.1
    scaleVolume = volume * 200
    if volume > 1:
        volume = 1
    mixer.music.set_volume(volume)
    canvas.delete("volume_bar")
    canvas.create_rectangle(100, 50, 100 + scaleVolume, 80, fill='red', tags="volume_bar")