from mutagen.mp3 import MP3
from globals import *

def songDataSecond():
    selectedSong = get_selected_song()
    songMetadata = MP3(f'./assets/songs/{selectedSong}')
    songSecond = songMetadata.info.length
    return(songSecond)

def songBar(font):
    print("test")
    roundBar = Py.Rect(480, 800, 20, 20)
    Py.draw.rect(screen, 'red', roundBar)
    text_surface = font.render("", True, 'white')
    text_rect = text_surface.get_rect(center=roundBar.center)
    screen.blit(text_surface, text_rect)