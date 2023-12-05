from tkinter import *
from testNewMember import *
from testMember import *
from PIL import Image, ImageTk

connectImage = None

def connect(root):
    global connectImage

    connect_window = Toplevel(root)
    connect_window.title('Connection')

    connectImage = Image.open("./images/bcgConnectImage.jpg")
    resizedConnect = connectImage.resize((400, 400))
    connectImage = ImageTk.PhotoImage(resizedConnect)

    canvas = Canvas(connect_window, width=resizedConnect.width, height=resizedConnect.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=connectImage)

    alreadyMember = Label(connect_window, text="Dejà membres ?", width=20)
    canvas.create_window(120, 50, anchor="nw", window=alreadyMember)

    userName = Label(connect_window, text="UserName")
    canvas.create_window(80, 80, anchor="nw", window=userName)

    userNameEntry = Entry(connect_window, bg='white', font=('Roboto', 10), fg="black", highlightcolor="white", width=20)
    canvas.create_window(180, 80, anchor="nw", window=userNameEntry)

    password = Label(connect_window, text="Mot de passe")
    canvas.create_window(80, 110, anchor="nw", window=password)

    passwordEntry = Entry(connect_window, bg='white', font=('Roboto', 10), fg="black", highlightcolor="white", show="*", width=20)
    canvas.create_window(180, 110, anchor="nw", window=passwordEntry)

    submitConnection = Button(connect_window, text="Submit", width=20, command=lambda : memberConnection(userNameEntry, passwordEntry, connect_window, canvas))
    canvas.create_window(120, 140, anchor="nw", window=submitConnection)

    newMember = Label(connect_window, text="Nouveau membre ?", width=20)
    canvas.create_window(120, 200, anchor="nw", window=newMember)

    nameNewMember = Label(connect_window, text="UserName")
    canvas.create_window(80, 230, anchor="nw", window=nameNewMember)

    nameNewEntry = Entry(connect_window, bg='white', font=('Roboto', 10), fg="black", highlightcolor="white", width=20)
    canvas.create_window(180, 230, anchor="nw", window=nameNewEntry)
    
    passwordNewMember = Label(connect_window, text="Mot de passe")
    canvas.create_window(80, 260, anchor="nw", window=passwordNewMember)

    passwordNewEntry = Entry(connect_window, bg='white', font=('Roboto', 10), fg="black", highlightcolor="white", width=20)
    canvas.create_window(180, 260, anchor="nw", window=passwordNewEntry)

    submitCreation = Button(connect_window, text="Submit", command=lambda :newMemberConnection(nameNewEntry, passwordNewEntry, connect_window, canvas), width=20)
    canvas.create_window(120, 290, anchor="nw", window=submitCreation)


# def read(filename):
#     with open(filename, 'r') as json_file:
#         json.load(json_file)
        
            
