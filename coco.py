# Créé par ivb, le 20/03/2017 en Python 3.2
import pygame
import tkinter
from tkinter import *
from pygame import mixer
from pygame import mixer
from tkinter.filedialog import askopenfilename

fenetre = Tk()
def set_filename():

    chemin = StringVar(fenetre)
    chemin = askopenfilename(filetypes=FILETYPES)
    print("chemin ",chemin)
    pygame.mixer.music.load(chemin)
    pygame.mixer.music.play()

FILETYPES = [ ("Fichiers musicaux", "*.mp3") ]
def precedent():
    a = 0
    a = pygame.mixer.music.get_pos()
    if a < 3:
        pygame.mixer.music.load(exchemin)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.rewind()
    print(a)
def stop():
    pygame.mixer.music.rewind()
    pygame.mixer.music.pause()

pygame.mixer.init()

cadre = Frame(fenetre, width=800, height=600, borderwidth=1)
cadre.pack(fill=BOTH)
cadre.configure(background='blue')
fenetre.configure(background='blue')

boutonParcourir = Button(fenetre, text='Parcourir', command=set_filename)
boutonParcourir.pack()

boutonPause = Button(fenetre, text="Pause", command=mixer.music.pause, fg="red", background = "#C8C8C8", height = "1", width = "4")
boutonPause.pack()

boutonPlay = Button(fenetre, text="Lecture", command = mixer.music.unpause, fg="black", background = "#FFFFFF", height = "3", width = "6")
boutonPlay.pack()

'''boutonPrecedent = Button(fenetre, text="Précédent", command = precedent(), fg="DARKBLUE", background = "#C8C8C8", height = "1", width = "5")
boutonPrecedent.pack()'''

boutonStop = Button(fenetre, text="Stop", command = stop(), fg="red", background = "#C8C8C8", height = "1", width = "4")
boutonStop.pack()

fenetre.mainloop()

pygame.mixer.quit()
