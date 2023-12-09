from pygame import mixer
from tkinter import *
from songWindow import *
from connect import *
from testNewMember import *
from burger import *
from PIL import Image, ImageTk

root = Tk()
root.title('Music player')

original_image = Image.open("./images/bcg_image.jpg")
resized_image = original_image.resize((400, 400))
original_image = ImageTk.PhotoImage(resized_image)

canvas = Canvas(root, width=resized_image.width, height=resized_image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=original_image)

signInImage = Image.open("./images/signIn.png")
ResizedSignIn = signInImage.resize((30, 30))
signInImage = ImageTk.PhotoImage(ResizedSignIn)

signInBtn = Button(root, image=signInImage, command=lambda: connect(root))
canvas.create_window(330, 20, anchor="nw", window=signInBtn)

title = Label(text="Let the music play !!!", fg="black", bg=root.cget('bg'))
canvas.create_window(150, 50, anchor="nw", window=title)

burger(root)

mainloop() 