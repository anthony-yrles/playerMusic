from pygame import mixer as mx
from globals import *
from playlist import *

def recule():
    print("j'en sais rien pour le moment")

def random():
    print("j'en sais rien pour le moment")

def play():
    mx.music.load(f'./assets/songs/{selectedSong}')
    mx.music.play()

def pauseFunct():
    global pause
    if not pause:
        mx.music.pause()
        pause = True
    else:
        mx.music.unpause()
        pause = False

def stopSong():
    mx.music.stop()

def advance():
    print("j'en sais rien pour le moment")

def loop():
    print("j'en sais rien pour le moment")

def volumeUp():
    global volume
    volume = volume + 0.1
    if volume > 1:
        volume = 1
    mx.music.set_volume(volume)

def volumeDown():
    global volume
    volume = volume - 0.1
    if volume  < 0:
        volume = 0
    mx.music.set_volume(volume)

def mute():
    volume = 0
    mx.music.set_volume(volume)