from tkinter import *
from jsonName import *

jsonName = 'nameAndPassword.json'

def newMemberConnection(nameNewEntry, passwordNewEntry, window, canvas):
    global jsonName
    autorisedChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*+=&"
    enteredText = nameNewEntry.get()
    enteredPassword = passwordNewEntry.get()
    enteredTextLower = enteredText.lower()

    if all(char in autorisedChar for char in enteredText) and all(char in autorisedChar for char in enteredPassword):
        try:
            with open(jsonName, 'r') as json_file:
                data = json.load(json_file)
                jsonNameLower = [entry[0].lower() for entry in data]

                if enteredTextLower in jsonNameLower:
                    refusedNameText = Label(window, text="Pseudo déjà utilisé", fg="red")
                    canvas.create_window(0, 320, anchor="nw", window=refusedNameText)
                    nameNewEntry.delete(0, 'end')
                    passwordNewEntry.delete(0, 'end')
                elif len(enteredPassword) < 8:
                    refusedPasswordText = Label(window, text="Password trop court au moins 8 caracteres necessaires", fg="red")
                    canvas.create_window(0, 320, anchor="nw", window=refusedPasswordText)
                    nameNewEntry.delete(0, 'end')
                    passwordNewEntry.delete(0, 'end')
                elif not any(char.isupper() for char in enteredPassword) or not any(char.islower() for char in enteredPassword):
                    refusedPasswordText = Label(window, text="Majuscule et minuscule nécessaires au mot de passe", fg="red")
                    canvas.create_window(0, 360, anchor="nw", window=refusedPasswordText)
                    nameNewEntry.delete(0, 'end')
                    passwordNewEntry.delete(0, 'end')
                else:
                    nameAndPassword = [enteredText, enteredPassword]
                    nameNewEntry.delete(0, 'end')
                    passwordNewEntry.delete(0, 'end')
                    save(jsonName, nameAndPassword, data)
        except FileNotFoundError:
            data = []
            nameAndPassword = [enteredText, enteredPassword]
            save(jsonName, nameAndPassword, data)
    else:
        refusedNameText = Label(window, text="Pseudo invalide", fg="red")
        canvas.create_window(120, 320, anchor="nw", window=refusedNameText)
        nameNewEntry.delete(0, 'end')
        passwordNewEntry.delete(0, 'end')