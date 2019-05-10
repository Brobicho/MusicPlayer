from tkinter import *

Window = Tk()
Label1 = Label(Window, text = 'Bonjour tout le monde !', fg = 'red')
Label1.pack()

# Création d'un widget Button (bouton Quitter)
btn = Button(Window, text = 'Quitter', command = Window.destroy)
btn.pack()

# Lancement du gestionnaire d'événements
Window.mainloop()
