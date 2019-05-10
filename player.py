from tkinter import *
import os
import tkinter.messagebox
import tkinter.filedialog

def Ouvrir():
    file = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",filetypes=[('audio files','.mp3', '.mp4', '.wav', '.flac', '.wma'),('all files','.*')])
    filename, file_extension = os.path.splitext(file)
    print(file)
    print(filename)
    print(file_extension)
    #window.title("SMP - " + str(photo.width()) + " x " + str(photo.height()))

def Fermer():
    window.title("SMP")

def Apropos():
    tkinter.messagebox.showinfo("A propos","Simple python music player made by brobicho")

# Main window
window = Tk()
window.title("SMP")

# Création d'un widget Menu
menubar = Menu(window)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir un fichier",command=Ouvrir)
menufichier.add_command(label="Quitter", command=window.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
window.config(menu=menubar)


window.mainloop()