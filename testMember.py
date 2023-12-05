from tkinter import *
import json

jsonName = 'nameAndPassword.json'

def memberConnection(userNameEntry, passwordEntry, window, canvas):
    global jsonName
    enteredText = userNameEntry.get()
    print(enteredText)
    enteredPassword = passwordEntry.get()
    print(enteredPassword)

    with open(jsonName, 'r') as json_file:
        data = json.load(json_file)
        jsonNameData = [entry[0] for entry in data]
        print(jsonNameData)
        jsonPasswordData = [entry[1] for entry in data]
        print(jsonPasswordData)

        if enteredText in jsonNameData:
            index = jsonNameData.index(enteredText)
            if enteredPassword == jsonPasswordData[index]:
                welcome = Label(window, text=f"Bienvenue {enteredText}", fg="red")
                canvas.create_window(0, 320, anchor="nw", window=welcome)
            else:
                notWelcome = Label(window, text="Mot de passe invalide", fg="red")
                canvas.create_window(0, 320, anchor="nw", window=notWelcome)
        else:
            notWelcome = Label(window, text="Login invalide", fg="red")
            canvas.create_window(0, 320, anchor="nw", window=notWelcome)
