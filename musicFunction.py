from pygame import mixer as mx
from globals import *
from playlist import *
import random

def recule():
    selectedSong = get_selected_song()
    if selectedSong is not None:
        index = songs.index(selectedSong)
        if index > 0:
            selectedSong = songs[index - 1]
            set_selected_song(selectedSong)
            print(selectedSong)
            play()

def rand():
    if songs:
        selectedSong = random.choice(songs)
        set_selected_song(selectedSong)
        print(selectedSong)
        mx.music.load(f'./assets/songs/{selectedSong}')
        mx.music.play()

def play():
    mx.music.load(f'./assets/songs/{get_selected_song()}')
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
    selectedSong = get_selected_song()
    if selectedSong is not None:
        index = songs.index(selectedSong)
        if index < len(songs) - 1:
            selectedSong = songs[index + 1]
            set_selected_song(selectedSong)
            print(selectedSong)
            play()

def loop():
    print("loop")
    while selectedSong is not None:
        play()

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