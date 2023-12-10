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

def play(font):
    selectedSong = get_selected_song()
    if selectedSong is not None:
        mx.music.load(f'./assets/songs/{selectedSong}')
        mx.music.play()
        songBar(font)
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