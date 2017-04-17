# Créé par ivb, le 20/03/2017 en Python 3.2
import pygame
import tkinter
from tkinter import *
from pygame import mixer


pygame.mixer.init()
chemin = input("BETA chemin du fichier")
pygame.mixer.music.load(chemin)
pygame.mixer.music.play()
fenetre = Tk()

photo = PhotoImage(file="Q:/Espace d'échange/Projets ISN/Lecteur MP3/images.png")

cadre = Frame(fenetre, width=800, height=600, borderwidth=1)
cadre.pack(fill=BOTH)
cadre.configure(background='blue')
fenetre.configure(background='blue')
boutonPause = Button(fenetre, text="Pause", command=mixer.music.pause, fg="red", background = "#C8C8C8", height = "1", width = "4")
boutonPause.pack()
boutonPlay = Button(root, fenetre, command = mixer.music.unpause, image = photo)
boutonPlay.pack()
boutonDebut = Button(fenetre, text="Début", command = mixer.music.play, fg="DARKBLUE", background = "#C8C8C8", height = "1", width = "5")
boutonDebut.pack()
boutonStop = Button(fenetre, text="Stop", command = mixer.music.stop, fg="red", background = "#C8C8C8", height = "1", width = "4")
boutonStop.pack()
fenetre.mainloop()
pygame.mixer.quit()
