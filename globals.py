import pygame as Py
import os

selectedSong = None

screen = Py.display.set_mode((800, 600))
width = 800
height = 600

def set_selected_song(song):
	global selectedSong
	selectedSong = song

def get_selected_song():
	global selectedSong
	return selectedSong

songs = os.listdir('./assets/songs') 

rect = Py.Rect(220, 510, 560, 60)
rectPlayList = Py.Rect(20, 20, 160, 35)
textePlaylist = "Playlist"
rectSound = Py.Rect (730, 100, 40, 280)
rectSongBar = Py.Rect(240, 470, 470, 20)

image = Py.image.load('./assets/images/bcg_image.jpg').convert_alpha()

imageRecule = Py.image.load('./assets/images/recule.png').convert_alpha()
imageReculePosition = (240, 520)

imageRandom = Py.image.load('./assets/images/random.png').convert_alpha()
imageRandomPosition = (320, 520)

imagePlay = Py.image.load('./assets/images/play.png').convert_alpha()
imagePlayPosition = (400, 520)

imagePause = Py.image.load('./assets/images/pause.png').convert_alpha()
imagePausePosition = (480, 520)

imageStop = Py.image.load('./assets/images/stop.png').convert_alpha()
imageStopPosition = (560, 520)

imageLoop = Py.image.load('./assets/images/loop.png').convert_alpha()
imageLoopPosition = (640, 520)

imageAdvance = Py.image.load('./assets/images/advance.png').convert_alpha()
imageAdvancePosition = (720, 520)

imageUp = Py.image.load('./assets/images/up.png').convert_alpha()
imageUpPosition = (730, 50)

imageDown = Py.image.load('./assets/images/down.png').convert_alpha()
imageDownPosition = (730, 400)

imageMute = Py.image.load('./assets/images/mute.png').convert_alpha()
imageMutePosition = (730, 450)

imageDownload = Py.image.load('./assets/images/download.png')
imageDownloadPosition = (220, 50)

imageTrash = Py.image.load('./assets/images/trash.png')
imageTrashPosition = (220, 100)

pause = False
volume = 0.5

# rectSound = Py.Rect(1220, 80 + 520 * volume, 20, 520 * volume)
# rectColor = (127.5 - 255 * volume ,127.5 + 255 * volume,0)

