from globals import *

def generatePlaylist(font, event):
    for index, song in enumerate(songs):
        rectIndex = Py.Rect(20, 25 + (50 * (index + 1)), 160, 40)
        rectIndexPosition = (20, 25 + (50 * (index + 1)))
        rectIndexWidth = 260
        rectIndexHeight = 40

        if get_selected_song() == song:
            background_color = 'red'
            text_color = 'white'
        else:
            background_color = 'gray'
            text_color = (0, 0, 0)

        Py.draw.rect(screen, background_color, rectIndex, 0, 15)
        text_surface = font.render(song, True, text_color)
        text_rect = text_surface.get_rect(center=rectIndex.center)
        screen.blit(text_surface, text_rect)

        selected = selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song)
        if selected is not None:
            set_selected_song(selected)
            print(get_selected_song())


def selection(event, rectIndexPosition, rectIndexWidth, rectIndexHeight, song):
    if event.type == Py.MOUSEBUTTONUP:
            if rectIndexPosition[0] <= event.pos[0] <= rectIndexPosition[0] + rectIndexWidth and \
               rectIndexPosition[1] <= event.pos[1] <= rectIndexPosition[1] + rectIndexHeight:
                return(song)
    return None     