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

LARGEUR = 1194
HAUTEUR = 834
COUL_FOND = "#ddd0b6"
COUL_FOND_2 = "#1b1b1b"
COUL_FOND_3 = "#292929"
COUL_QUADR = "#99958d"
COTE = 47

liste_obstacles = ["2", "G", "3"]

liste = []
with open("map.txt") as f:
    for line in f.readlines():
        liste.append(list(line[:-1]))


def dessiner_obstacles():
    for i in range(len(liste)):
        if i == 0 or i == 32:
            pass
        elif i % 2 == 1:
            for j in range(1, 32):
                if liste[i][j] == "3":
                    canvas.create_rectangle(
                        37 + j//2 * 47, 41 + i//2 * 47, 45 + j//2 * 47, 41 + (i//2 + 1) * 47, fill='black'
                    )
        else:
            for j in range(1, 32):
                if liste[i][j] == "3":
                    canvas.create_rectangle(
                        41 + j//2 * 47, 37 + i//2 * 47, 41 + (j//2 + 1) * 47, 45 + i//2 * 47, fill='black'
                    )


def affiche_liste(liste):
    for sous_liste in liste:
        for element in sous_liste:
            print(element, end=" ")
        print()


def quadrillage():
    """Dessine un quadrillage formé de carrés de côté COTE"""
    y = 41
    while y <= 793:
        canvas.create_line((41, y), (793, y), fill=COUL_QUADR)
        y += COTE
    x = 41
    while x <= 793:
        canvas.create_line((x, 41), (x, 793), fill=COUL_QUADR)
        x += COTE


def calculer_position(x, y):
    return [(x*2+1, y*2+1), (x, y), deplacement_possible(x*2+1, y*2+1)]


def deplacement_possible(x, y):
    up, down, left, right = 0, 0, 0, 0
    index = x
    while liste[index-1][y] not in liste_obstacles:
        up += 1
        index -= 1
        print(liste[index-1][y])
    index = x
    while liste[index+1][y] not in liste_obstacles:
        down += 1
        index += 1
    index = y
    while liste[x][index-1] not in liste_obstacles:
        left += 1
        index -= 1
    index = y
    while liste[x][index+1] not in liste_obstacles:
        right += 1
        index += 1
    return up//2, down//2, left//2, right//2


def create_rectangle_en_fonction_de_position(position, color):
    return canvas.create_oval(44 + COTE*position[1], 44 + COTE*position[0], 84 + COTE*position[1], 84 + COTE*position[0], fill=color)


def renouveler_position_dans_liste():
    global info_bot_red, liste

    x, y = info_bot_red[0]
    info_bot_red = calculer_position(info_bot_red[1][0], info_bot_red[1][1]) + [info_bot_red[-1]]
    print(info_bot_red)
    
    liste[info_bot_red[0][0]][info_bot_red[0][1]] = liste[x][y]
    liste[x][y] = 0
    affiche_liste(liste)


def deplacement(event):
    key =  event.keysym
    if key == "Up":
        mouvement_up(event)
    elif key == "Down":
        mouvement_down(event)
    elif key == "Right":
        mouvement_right(event)
    elif key == "Left":
        mouvement_left(event)


def mouvement_up(event):
    global info_bot_red, liste
    canvas.move(bot_red, 0, -info_bot_red[2][0] * 47)

    info_bot_red[1] = (info_bot_red[1][0]- info_bot_red[2][0], info_bot_red[1][1])
    if info_bot_red[2][0] != 0:
        renouveler_position_dans_liste()


def mouvement_down(event):
    global info_bot_red
    canvas.move(bot_red, 0, info_bot_red[2][1] * 47)
    info_bot_red[1] = (info_bot_red[1][0] + info_bot_red[2][1], info_bot_red[1][1])

    if info_bot_red[2][1] != 0:
        renouveler_position_dans_liste()


def mouvement_left(event):
    global info_bot_red
    canvas.move(bot_red, -info_bot_red[2][2] * 47, 0)
    info_bot_red[1] = (info_bot_red[1][0], info_bot_red[1][1] - info_bot_red[2][2])

    if info_bot_red[2][2] != 0:
        renouveler_position_dans_liste()


def mouvement_right(event):
    global info_bot_red
    canvas.move(bot_red, info_bot_red[2][3] * 47, 0)
    info_bot_red[1] = (info_bot_red[1][0], info_bot_red[1][1] + info_bot_red[2][3])

    if info_bot_red[2][3] != 0:
        renouveler_position_dans_liste()


root = tk.Tk()
root.title('Robot Ricochet')
root.geometry(f"{LARGEUR+10}x{HAUTEUR+10}")
root.configure(bg=COUL_FOND_2)
root.resizable(False, False)

canvas = tk.Canvas(height=HAUTEUR, width=LARGEUR, bg=COUL_FOND_2)
canvas.grid()
canvas.create_rectangle(33, 33, 801, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(41, 41, 793, 793, fill=COUL_FOND)
quadrillage()

canvas.create_rectangle(830, 33, 1160, 298, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(830, 340, 925, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(947, 340, 1043, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(1065, 340, 1160, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
canvas.create_rectangle(830, 441, 1160, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)


info_bot_red = calculer_position(7, 13) + ["red"]
info_bot_green = calculer_position(5, 0) + ["green"]


bot_red = create_rectangle_en_fonction_de_position(info_bot_red[1], "red")
bot_green = create_rectangle_en_fonction_de_position(info_bot_green[1], "green")

dessiner_obstacles()

canvas.bind_all("<Key>", deplacement)

root.mainloop()