from globals import *
import os

songs = os.listdir('./assets/songs')  

def generatePlaylist(font, event):
    for index, song in enumerate(songs):
        rectIndex = Py.Rect(20, 25 + (50 * (index + 1)), 260, 40)
        rectIndexPosition = (20, 25 + (50 * (index + 1)))
        rectIndexWidth = 260
        rectIndexHeight = 40
        Py.draw.rect(screen, 'gray', rectIndex)
        text_surface = font.render(song, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rectIndex.center)
        screen.blit(text_surface, text_rect)

        selected = selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song)
        if selected is not None:
            selectedSong = selected
            set_selected_song(selectedSong)
            print(selectedSong)

        if index == len(songs) - 1:
            text_surface = font.render(song, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rectIndex.center)
            screen.blit(text_surface, text_rect)
            rectDownload = Py.Rect(20, 25 + (50 * (index + 2)), 260, 40)
            Py.draw.rect(screen, 'gray', rectDownload)
            text_surface = font.render("Download", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rectDownload.center)
            screen.blit(text_surface, text_rect)

def selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song):
    if event.type == Py.MOUSEBUTTONUP:
            if rectIndexPosition[0] <= event.pos[0] <= rectIndexPosition[0] + rectIndexWidth and \
               rectIndexPosition[1] <= event.pos[1] <= rectIndexPosition[1] + rectIndexHeight:
                return(song)
    return None     