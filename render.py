from globals import *
from playlist import *
from buttonFunction import *

def render(font):
    screen.blit(image, (200,0))

    Py.draw.rect(screen, 'gray', rectPlayList, 0, 15)
    text_surface = font.render(textePlaylist, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rectPlayList.center)
    screen.blit(text_surface, text_rect)

    Py.draw.rect(screen, 'gray', rect, 0, 30)
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
    screen.blit(imageDownload, imageDownloadPosition)
    screen.blit(imageTrash, imageTrashPosition)
    # Py.draw.rect(screen, rectColor, rectSound, 0, 15)

    Py.display.flip()