from tkinter.filedialog import askopenfilename

def set_filename():
    chemin = StringVar(fenetre)
    chemin = askopenfilename(filetypes=FILETYPES)
    pygame.mixer.music.load(chemin)
    pygame.mixer.music.play()

FILETYPES = [ ("Fichiers musicaux", "*.mp3") ]

boutonParcourir = Button(fenetre, text='Parcourir', command=set_filename)
boutonParcourir.place(x=280,y=140)
