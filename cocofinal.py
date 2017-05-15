import pygame
import tkinter
from tkinter import *
from pygame import mixer
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import mutagen
import os
import csv
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
mutagen.File("musique.mp3")

def set_filename():

    chemin = StringVar(fenetre)
    chemin = askopenfilename(filetypes=FILETYPES)

    pygame.mixer.music.load(chemin)
    pygame.mixer.music.play()
    txtArtist()

FILETYPES = [ ("Fichiers musicaux", "*.mp3") ]

pygame.mixer.init()
#configuration de la fenêtre
fenetre = Tk()
fenetre.geometry("600x200+600+400")
fenetre.title("Lecteur MP3")

#Pour mettre l'image de fond
fond = PhotoImage(file="fond.png")
Largeur = 600
Hauteur = 200
Canevas = Canvas(fenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=fond)
Canevas.place(x=0,y=0)

def Volume() :
    fenetre.after(50,Volume)     #50 ms entre les changements de son
    vol1 = Boutonvolume.get()    #Prendre la valeur du Volume
    pygame.mixer.music.set_volume(vol1*.01)  #Donne la valeur a la variable vol

def Mute():
    Boutonvolume.set(0)

fenetre.after(100,Volume) # on met le volume a 100 au début

#Mise en place du cotrôle du volume
texte=Label(fenetre,text="Volume",bg='#FFFFFF')
texte.place(x=15,y=160)

def txtArtist():
    audio = EasyID3(musique)
    artiste = audio['artist'][0]
    artist = Label(fenetre, text = artiste, bg='#FFFFFF')
    artist.place(x=405, y=155)

boutonPause = Button(fenetre,command=mixer.music.pause,height = 40, width = 40)
boutonPause.place(x='285',y='70')
pause = PhotoImage(file = 'PAUSE.png')
boutonPause.config(image= pause)


boutonPlay = Button(fenetre,command = mixer.music.unpause, height = 40, width = 40)
boutonPlay.place(x='235',y='70')
play= PhotoImage(file='PLAY.png')
boutonPlay.config(image=play)



boutonDebut = Button(fenetre, command = mixer.music.play, height = 40, width = 40)
boutonDebut.place(x='185',y='70')
debut= PhotoImage(file='PRECEDENT.png')
boutonDebut.config(image=debut)

boutonStop = Button(fenetre, command = mixer.music.stop, height = 40, width = 40)
boutonStop.place(x='335',y='70')
stop= PhotoImage(file='STOP.png')
boutonStop.config(image=stop)

boutonSuivant = Button(fenetre, command = mixer, height = 40, width = 40)
boutonSuivant.place(x='385',y='70')
suivant=PhotoImage(file='SUIVANT.png')
boutonSuivant.config(image=suivant)


Boutonvolume = Scale(fenetre, from_=100, to=0,fg='white', bg='black')
Boutonvolume.set(100)
Boutonvolume.pack(side = LEFT, padx = 15, pady = 15)


BoutonMute = Button(fenetre, command = Mute, height=30, width=30)
BoutonMute.place(x=20,y=8)
mute=PhotoImage(file='MUTE.png')
BoutonMute.config(image=mute)

boutonParcourir = Button(fenetre, text='Parcourir', command=set_filename)
boutonParcourir.place(x=280,y=140)

progress = IntVar(0)
barre = ttk.Progressbar(fenetre,orient=HORIZONTAL, length=250,maximum = 100, mode='determinate',variable = progress)
barre.place(x=185,y=170)

def step():
    progress.set(pygame.mixer.music.get_pos() / audio.info.length /10 )
    fenetre.after(50, step)

'''step()'''


fenetre.mainloop()
pygame.mixer.quit()
