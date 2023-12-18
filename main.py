import pygame as Py
from render import *
from button import *
from playlist import *
from globals import *

Py.init()

continuer = True
font = Py.font.Font("./assets/font/Roboto-Black.ttf", 18)

while continuer:
    render(font)
    for event in Py.event.get():
        if event.type == Py.QUIT:
            continuer = False
        generatePlaylist(font, event)
        songSecond = songDataSecond()
        reculeButton(event)
        randomButton(event)
        playButton(event)
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