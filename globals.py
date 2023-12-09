import pygame as Py

selectedSong = None

screen = Py.display.set_mode((1300, 1000))
width = 1300
height = 1000

def set_selected_song(song):
	global selectedSong
	selectedSong = song

def get_selected_song():
	global selectedSong
	return selectedSong

rect = Py.Rect(460, 890, 700, 80)
rectPlayList = Py.Rect(20, 20, 260, 40)
textePlaylist = "Playlist"

image = Py.image.load('./assets/images/bcg_image.jpg').convert_alpha()

imageRecule = Py.image.load('./assets/images/recule.png').convert_alpha()
imageReculePosition = (480, 900)

imageRandom = Py.image.load('./assets/images/random.png').convert_alpha()
imageRandomPosition = (580, 900)

imagePlay = Py.image.load('./assets/images/play.png').convert_alpha()
imagePlayPosition = (680, 900)

imagePause = Py.image.load('./assets/images/pause.png').convert_alpha()
imagePausePosition = (780, 900)

imageStop = Py.image.load('./assets/images/stop.png').convert_alpha()
imageStopPosition = (880, 900)

imageAdvance = Py.image.load('./assets/images/advance.png').convert_alpha()
imageAdvancePosition = (980, 900)

imageLoop = Py.image.load('./assets/images/loop.png').convert_alpha()
imageLoopPosition = (1080, 900)

imageUp = Py.image.load('./assets/images/up.png').convert_alpha()
imageUpPosition = (1200, 50)

imageDown = Py.image.load('./assets/images/down.png').convert_alpha()
imageDownPosition = (1200, 650)

imageMute = Py.image.load('./assets/images/mute.png').convert_alpha()
imageMutePosition = (1200, 750)

pause = False
volume = 0.5

