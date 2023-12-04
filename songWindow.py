from tkinter import *
from PIL import Image, ImageTk

def newSongWindow(song, root):
    song_window = Toplevel(root)
    song_window.title(song)

    song_bcg = Image.open('./images/song_bcg.png')
    resized_song_bcg = song_bcg.resize((400, 400))
    background_photo = ImageTk.PhotoImage(resized_song_bcg)

    canvas = Canvas(song_window, width=resized_song_bcg.width, height=resized_song_bcg.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    playBtn = Button(song_window, text="   Play   ")
    canvas.create_window(20, 330, anchor="nw", window=playBtn)

    pauseBtn = Button(song_window, text="  Pause  ")
    canvas.create_window(120, 330, anchor="nw", window=pauseBtn)

    stopBtn = Button(song_window, text="   Stop   ")
    canvas.create_window(220, 330, anchor="nw", window=stopBtn)

    resumeBtn = Button(song_window, text="  Resume  ")
    canvas.create_window(320, 330, anchor="nw", window=resumeBtn)

    volumeDownBtn = Button(song_window, text="  Réduire ")
    canvas.create_window(70, 370, anchor="nw", window=volumeDownBtn)

    volumeUpBtn = Button(song_window, text=" Augmenter")
    canvas.create_window(170, 370, anchor="nw", window=volumeUpBtn)

    songLoopBtn = Button(song_window, text="  Boucle  ")
    canvas.create_window(270, 370, anchor="nw", window=songLoopBtn)