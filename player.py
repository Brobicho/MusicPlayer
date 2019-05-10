from tkinter import *
#import os
import ntpath
import pygame
import tkinter.messagebox
import tkinter.filedialog
#import mutagen

def Ouvrir():
    file = tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",filetypes=[('audio files', '.mp3'),('audio files', '.wav'),('audio files', '.flac'),('audio files', '.ogg'),('audio files', '.mp4'),('all files','.*')])
    filename = ntpath.basename(file)
    Loadmeta(filename)
    Playfile(file)

def Playfile(file):
    pygame.mixer.init(44100, -16, 2, 4096)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def Loadmeta(file):
    window.title("SMP - Playing " + file + " ♪")

def Fermer():
    window.title("SMP")

def Apropos():
    tkinter.messagebox.showinfo("A propos","Simple python music player made by brobicho")

# Main window
window = Tk()
window.title("SMP")
window.iconbitmap(r'C:\Users\Flantier\Desktop\MusicPlayer\music-album.ico')

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