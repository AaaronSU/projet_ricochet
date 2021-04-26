#########################################
# groupe MPCI 7
# Yingqin SU
# Mohamed Hachour
# Djibril-Hamed ALABY
# Yassine Chaouch
# Jonathan Van
# Adel SIFI
# https://github.com/Yingqin-SU/projet_ricochet
#########################################

import tkinter as tk

#########constantes########
LARGEUR = 1194
HAUTEUR = 834
COUL_FOND = "#ddd0b6"
COUL_FOND_2 = "#1b1b1b"
COUL_FOND_3 = "#292929"
COUL_QUADR = "#99958d"
COTE = 47

########fonctions##########
def quadrillage():
    """Dessine un quadrillage formé de carrés de côté de taille COTE"""
    y = 41
    while y <= 793:
        canvas.create_line((41, y), (793, y), fill=COUL_QUADR)
        y += COTE
    x = 41
    while x <= 793:
        canvas.create_line((x, 41), (x, 793), fill=COUL_QUADR)
        x += COTE

def deplacement(event):
    key =  event.keysym
    if key == "Up":
        canvas.move(boule_bleu, 0, -47)
    elif key == "Down":
        canvas.move(boule_bleu, 0, +47)
    elif key == "Right":
        canvas.move(boule_bleu, +47, 0)
    elif key == "Left":
        canvas.move(boule_bleu, -47, 0)

###programme principale###
root = tk.Tk()
root.title('Robot Ricochet')
root.geometry(f"{LARGEUR+10}x{HAUTEUR+10}")
root.configure(bg=COUL_FOND_2)
root.resizable(False, False)

###création et placement des widgets###
canvas = tk.Canvas(height=HAUTEUR, width=LARGEUR, bg=COUL_FOND_2)
canvas.create_rectangle(33, 33, 801, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(41, 41, 793, 793, fill=COUL_FOND)
canvas.create_rectangle(830, 33, 1160, 298, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(830, 340, 925, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(947, 340, 1043, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(1065, 340, 1160, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(830, 441, 1160, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)
boule_bleu = canvas.create_oval(276, 511, 323, 558, fill="blue")
boule_verte = canvas.create_oval(464, 88, 511, 135, fill="green")
boule_jaune = canvas.create_oval(276, 652, 323, 699, fill="yellow")
boule_rouge = canvas.create_oval(746, 182, 793, 229, fill="red")
quadrillage()
canvas.create_rectangle(370, 370, 464, 464, fill="black")
canvas.grid()

###autres###
canvas.bind_all("<Key>", deplacement)

###boucle infini###
root.mainloop()