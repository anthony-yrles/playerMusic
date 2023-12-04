from pygame import mixer
from tkinter import *
from PIL import Image, ImageTk
from songWindow import *
import os

root = Tk()
root.title('Music player')

original_image = Image.open("./images/bcg_image.jpg")
resized_image = original_image.resize((400, 400))
background_photo = ImageTk.PhotoImage(resized_image)

canvas = Canvas(root, width=resized_image.width, height=resized_image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=background_photo)

title = Label(text="Let the music play !!!", fg="black", bg=root.cget('bg'))
canvas.create_window(150, 50, anchor="nw", window=title)

mixer.init()
volume = 0.5
mixer.music.set_volume(volume)

songs = os.listdir('./songs')
song_buttons = {}

for index, song in enumerate(songs):
    song_buttons[index] = Button(root, text=song, command=lambda: newSongWindow(song[index], root))
    canvas.create_window(20 + (80 * (index + 1)), 300, anchor="nw", window=song_buttons[index])

mainloop() 