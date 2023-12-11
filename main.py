# Initialisation pygame
# Choix des variables et des assets de la fenetre pygame
# Ouverture de la fenetre
# Gestion de la fermeture de la page.
# Créationn des boutons facile (play, pause, stop, volumeup, volume down)
# Fonction play, pause, stop, volumeup, volumedown
# Bouton avancé lecture en boucle, aléatoire
# Fonction playLoop, playRandom
# Création playlist
# Fonction selectSong
# Bouton  + fonction donwload
# Travail esthetique de la fenetre
# Création barre de défilement de la musique.

import pygame as Py
from render import *
from button import *
from playlist import *
from globals import *

Py.init()

continuer = True
# script_folder = os.path.dirname(os.path.abspath("C:\\Users\\Anthony\\OneDrive\\Bureau\\playerMusic\\assets"))
# font_path = os.path.join(script_folder, 'assets', 'font', 'Roboto-Black.ttf')
font = Py.font.Font("./assets/font/Roboto-Black.ttf", 18)

while continuer:
    render(font)
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        generatePlaylist(font, event)
        reculeButton(event)
        randomButton(event)
        playButton(event, font)
        pauseButton(event)
        stopButton(event)
        advanceButton(event)
        loopButton(event)
        upButton(event)
        downButton(event)
        muteButton(event)
        downloadButton(event, font)
        trashButton(event, font)
Py.quit()