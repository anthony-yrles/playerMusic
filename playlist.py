from globals import *

def generatePlaylist(font, event):
    for index, song in enumerate(songs):
        rectIndex = Py.Rect(20, 25 + (50 * (index + 1)), 260, 40)
        rectIndexPosition = (20, 25 + (50 * (index + 1)))
        rectIndexWidth = 260
        rectIndexHeight = 40
        Py.draw.rect(screen, 'gray', rectIndex, 0, 15)
        text_surface = font.render(song, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rectIndex.center)
        screen.blit(text_surface, text_rect)

        selected = selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song)
        if selected is not None:
            selectedSong = selected
            set_selected_song(selectedSong)
            Py.draw.rect(screen, 'red', rectIndex)
            text_surface = font.render(song, True, 'white')
            text_rect = text_surface.get_rect(center=rectIndex.center)
            screen.blit(text_surface, text_rect)
            print(selectedSong)

def selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song):
    if event.type == Py.MOUSEBUTTONUP:
            if rectIndexPosition[0] <= event.pos[0] <= rectIndexPosition[0] + rectIndexWidth and \
               rectIndexPosition[1] <= event.pos[1] <= rectIndexPosition[1] + rectIndexHeight:
                return(song)
    return None     