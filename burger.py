from tkinter import *
from songWindow import *
import os

def burger(window):
    songBar = Menu(window)
    window.config(menu=songBar)    
    songList = Menu(songBar ,tearoff=0)
    songs = os.listdir('./songs')

    for index, song in enumerate(songs):
        songList.add_command(label=songs[index], command=lambda: newSongWindow(songs[index], window))
    songBar.add_cascade(label="Bibilotheque", menu=songList)

    favBar = Menu(songBar, tearoff=0)

    for index, song in enumerate(songs):
        favBar.add_command(label=songs[index])
    songBar.add_cascade(label="Playlist", menu=favBar)
