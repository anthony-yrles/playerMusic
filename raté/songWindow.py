from tkinter import *
from mixerFunct import *
from PIL import Image, ImageTk

# Variables globales pour les images
playImage = None
pauseImage = None
downImage = None
upImage = None
songBcg = None

def newSongWindow(song, root):
    global playImage, pauseImage, downImage, upImage, songBcg, canvas

    song_window = Toplevel(root)
    song_window.title(song)

    songBcg = Image.open('./images/song_bcg.png')
    songBcgResize = songBcg.resize((400, 400))
    songBcg = ImageTk.PhotoImage(songBcgResize)

    canvas = Canvas(song_window, width=songBcgResize.width, height=songBcgResize.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=songBcg)

    if playImage is None:
        playImage = Image.open('./images/play.png')
        playImage = playImage.resize((30, 30))
        playImage = ImageTk.PhotoImage(playImage)

    if pauseImage is None:
        pauseImage = Image.open('./images/pause.png')
        pauseImage = pauseImage.resize((30, 30))
        pauseImage = ImageTk.PhotoImage(pauseImage)

    if downImage is None:
        downImage = Image.open('./images/down.png')
        downImage = downImage.resize((30, 30))
        downImage = ImageTk.PhotoImage(downImage)

    if upImage is None:
        upImage = Image.open('./images/up.png')
        upImage = upImage.resize((30, 30))
        upImage = ImageTk.PhotoImage(upImage)

    mixer.init()
    mixer.music.set_volume(volume)
    

    playBtn = Button(song_window, image=playImage, command=lambda: playSong(song))
    canvas.create_window(20, 350, anchor="nw", window=playBtn)

    pauseBtn = Button(song_window, image=pauseImage, command=lambda: pauseSong())
    canvas.create_window(120, 350, anchor="nw", window=pauseBtn)

    volumeUpBtn = Button(song_window, image=upImage, command=lambda: volumeUp(canvas))
    canvas.create_window(315, 45, anchor="nw", window=volumeUpBtn)

    volumeDownBtn = Button(song_window, image=downImage, command=lambda: volumeDown(canvas))
    canvas.create_window(50, 45, anchor="nw", window=volumeDownBtn)




    # stopImage = Image.open('./images/stop.png')
    # stopImage = ImageTk.PhotoImage(stopImage)

    # stopBtn = Button(song_window, image=stopImage)
    # canvas.create_window(80, 350, anchor="nw", window=stopBtn)

    # songLoopBtn = Button(song_window, image="./images/pause.png")
    # canvas.create_window(270, 370, anchor="nw", window=songLoopBtn)