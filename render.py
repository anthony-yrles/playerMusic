from globals import *
from playlist import *

def render(font):
    screen.blit(image, (300,0))

    Py.draw.rect(screen, 'gray', rectPlayList)
    text_surface = font.render(textePlaylist, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rectPlayList.center)
    screen.blit(text_surface, text_rect)

    Py.draw.rect(screen, 'gray', rect)
    screen.blit(imageRecule, imageReculePosition)
    screen.blit(imageRandom, imageRandomPosition)
    screen.blit(imagePlay, imagePlayPosition)
    screen.blit(imagePause, imagePausePosition)
    screen.blit(imageStop, imageStopPosition)
    screen.blit(imageAdvance, imageAdvancePosition)
    screen.blit(imageLoop, imageLoopPosition)
    screen.blit(imageUp, imageUpPosition)
    screen.blit(imageDown, imageDownPosition)
    screen.blit(imageMute, imageMutePosition)

    Py.display.flip()