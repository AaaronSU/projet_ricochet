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

LARGEUR = 800
HAUTEUR = 800
COUL_FOND = "#ddd0b6"
COUL_QUADR = "#99958d"
COTE = 50


def quadrillage():
    """Dessine un quadrillage formé de carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COUL_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COUL_QUADR)
        x += COTE


root = tk.Tk()
root.title('Robot Ricochet')
root.resizable(False, False)
canvas = tk.Canvas(height=HAUTEUR, width=LARGEUR, bg=COUL_FOND)
canvas.grid()
quadrillage()
canvas.create_rectangle(350, 345, 450, 455, fill='black')
canvas.create_rectangle(345, 350, 455, 450, fill='black')

root.mainloop()