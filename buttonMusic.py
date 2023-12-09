from musicFunction import *
from globals import *

def reculeButton(event):
     if event.type == Py.MOUSEBUTTONDOWN:
            if imageReculePosition[0] <= event.pos[0] <= imageReculePosition[0] + imageRecule.get_width() and \
               imageReculePosition[1] <= event.pos[1] <= imageReculePosition[1] + imageRecule.get_height():
                recule()

def randomButton(event):
     if event.type == Py.MOUSEBUTTONDOWN:
            if imageRandomPosition[0] <= event.pos[0] <= imageRandomPosition[0] + imageRandom.get_width() and \
               imageRandomPosition[1] <= event.pos[1] <= imageRandomPosition[1] + imageRandom.get_height():
                rand()

def playButton(event):
   if event.type == Py.MOUSEBUTTONDOWN:
      if imagePlayPosition[0] <= event.pos[0] <= imagePlayPosition[0] + imagePlay.get_width() and \
         imagePlayPosition[1] <= event.pos[1] <= imagePlayPosition[1] + imagePlay.get_height():
         selectedSong = get_selected_song()
         print(selectedSong)
         if selectedSong is not None:
            play()
               

def pauseButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imagePausePosition[0] <= event.pos[0] <= imagePausePosition[0] + imagePause.get_width() and \
               imagePausePosition[1] <= event.pos[1] <= imagePausePosition[1] + imagePause.get_height():
                pauseFunct()

def stopButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageStopPosition[0] <= event.pos[0] <= imageStopPosition[0] + imageStop.get_width() and \
               imageStopPosition[1] <= event.pos[1] <= imageStopPosition[1] + imageStop.get_height():
                stopSong()

def advanceButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageAdvancePosition[0] <= event.pos[0] <= imageAdvancePosition[0] + imageAdvance.get_width() and \
               imageAdvancePosition[1] <= event.pos[1] <= imageAdvancePosition[1] + imageAdvance.get_height():
                advance()

def loopButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageLoopPosition[0] <= event.pos[0] <= imageLoopPosition[0] + imageLoop.get_width() and \
               imageLoopPosition[1] <= event.pos[1] <= imageLoopPosition[1] + imageLoop.get_height():
                loop()

def upButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageUpPosition[0] <= event.pos[0] <= imageUpPosition[0] + imageUp.get_width() and \
               imageUpPosition[1] <= event.pos[1] <= imageUpPosition[1] + imageUp.get_height():
                volumeUp()

def downButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageDownPosition[0] <= event.pos[0] <= imageDownPosition[0] + imageDown.get_width() and \
               imageDownPosition[1] <= event.pos[1] <= imageDownPosition[1] + imageDown.get_height():
                volumeDown()

def muteButton(event):
    if event.type == Py.MOUSEBUTTONDOWN:
            if imageMutePosition[0] <= event.pos[0] <= imageMutePosition[0] + imageMute.get_width() and \
               imageMutePosition[1] <= event.pos[1] <= imageMutePosition[1] + imageMute.get_height():
                mute()