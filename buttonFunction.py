from pygame import mixer as mx
from globals import *
from playlist import *
from advancementBar import *
import random
from tkinter import filedialog as fd 
from tkinter import messagebox as mb

def recule():
    selectedSong = get_selected_song()
    if selectedSong is not None:
        index = songs.index(selectedSong)
        if index > 0:
            selectedSong = songs[index - 1]
            set_selected_song(selectedSong)
            print(selectedSong)
            play()
    else:
        mb.showerror("Erreur", "Veuillez sélectionner un fichier son avant")

def rand():
    if songs:
        selectedSong = random.choice(songs)
        set_selected_song(selectedSong)
        mx.music.load(f'./assets/songs/{selectedSong}')
        mx.music.play()

# def play(font):
def play():
    selectedSong = get_selected_song()
    if selectedSong is not None:
        mx.music.load(f'./assets/songs/{selectedSong}')
        mx.music.play()
        # songBar(font)
    else:
        mb.showerror("Erreur", "Veuillez sélectionner un fichier son avant")

def pauseFunct():
    global pause
    selectedSong = get_selected_song()
    if selectedSong is not None:
        if not pause:
            mx.music.pause()
            pause = True
        else:
            mx.music.unpause()
            pause = False
    else:
        mb.showerror("Erreur", "Veuillez sélectionner un fichier son avant")

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
    else:
        mb.showerror("Erreur", "Veuillez sélectionner un fichier son avant")

import time

def loop(songSecond):
    selectedSong = get_selected_song()
    while selectedSong is not None:
        play()
        time.sleep(songSecond)  # Attendez 1 seconde avant de vérifier à nouveau la chanson sélectionnée
        selectedSong = get_selected_song()


def volumeUp():
    volume_new = get_selected_volume() + 0.1
    if volume_new > 1:
        volume_new = 1
    set_selected_volume(volume_new)
    Py.draw.rect(screen, rectColor, rectSound, 0, 15)
    mx.music.set_volume(get_selected_volume())

def volumeDown():
    volume_new = get_selected_volume() - 0.1
    if volume_new  < 0:
        volume_new = 0
    set_selected_volume(volume_new)
    Py.draw.rect(screen, rectColor, rectSound, 0, 15)
    mx.music.set_volume(get_selected_volume())

def mute():
    volume_new = 0
    set_selected_volume(volume_new)
    mx.music.set_volume(get_selected_volume())

def downloads(font, event):
    file = fd.askopenfile()
    audio_extensions = ['.mp3', '.wav', '.ogg']
    filename = os.path.basename(file.name)
    _, extension = os.path.splitext(filename)
    if extension.lower() in audio_extensions:
        if filename not in songs:
            songs.append(filename)
            generatePlaylist(font, event)
    else:
        mb.showerror("Erreur", "Le fichier sélectionné n'est pas un fichier son valide.")
    file.close()

def trash(font, event):
    selectedSong = get_selected_song()
    if selectedSong is not None:
        response = mb.askquestion("Confirmation", f"Voulez-vous supprimer {selectedSong} de la liste de lecture?")
        if response == 'yes':
            songs.remove(selectedSong)
            generatePlaylist(font, event)