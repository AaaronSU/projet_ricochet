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
import tkinter.messagebox

LARGEUR = 1194
HAUTEUR = 834
COUL_FOND = "#ddd0b6"
COUL_FOND_2 = "#1b1b1b"
COUL_FOND_3 = "#292929"
COUL_QUADR = "#99958d"
ficher_enregistrement_et_chargement = "map.txt"
bot_controlling = "R"
COTE = 47
charger = False
success = False


def charger_map():
    global map_initial
    if charger:
        try:
            with open(ficher_enregistrement_et_chargement, "r") as f:
                map_initial = []
                nombre_ligne = 0
                for line in f.readlines():
                    if nombre_ligne < 5:
                        sous_map_initial = line[:-1].split(" ")
                        sous_map_initial = [int(element) for element in sous_map_initial]
                        map_initial.append(sous_map_initial)
                    elif nombre_ligne == 4:
                        sous_map_initial = line[:-1].split(" ")
                        sous_map_initial = [int(element) for element in sous_map_initial]
                        map_initial.append(sous_map_initial)
                    elif nombre_ligne == 5:
                        map_initial[-1].append(line[:-1])
                        map_initial.append([])
                    elif 5 < nombre_ligne < 39:
                        map_initial[-1].append(line[:-1])
                    
                    nombre_ligne += 1
                map_initial[4] = ((map_initial[4][0], map_initial[4][1]), map_initial[4][2])
        except:
            tkinter.messagebox.showerror("error", "Le fichier du chargement n'existe pas")
        else:
            tkinter.messagebox.showinfo("sucess", "Le map est chargé")
            root.destroy()
            main()
    else:
        map_initial = [
            (0, 0), # red
            (5, 0), # green
            (4, 10), # blue
            (8, 2), # yellow
            ((11, 1), "Y"),
            [
                "*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*",
                "201010301010101010101010301010102",
                "*1*1*1*1*1*1*1*1*1*1*1*1*1*3*1*1*",
                "201010101030101010101010103010102",
                "*1*1*1*1*1*3*1*1*1*1*1*1*1*1*1*1*",
                "201010101010101030103010101010102",
                "*1*1*1*1*1*1*1*3*1*3*1*1*1*1*1*1*",
                "201010101010101010101030101010102",
                "*3*1*1*1*1*1*1*1*1*1*1*3*1*1*1*3*",
                "201010103010101010101010101010102",
                "*1*1*1*3*1*1*3*1*1*1*1*1*1*1*1*1*",
                "201010101010301010101010101030102",
                "*1*3*1*1*1*1*1*1*1*1*1*3*1*1*3*1*",
                "201030101010101010101010301010102",
                "*1*1*1*1*1*1*1*3*3*1*1*1*1*1*1*1*",
                "201010101010103030301010101010102",
                "*1*1*1*1*1*1*1*3*3*1*1*1*1*1*1*1*",
                "201010101010103030301010101010102",
                "*1*1*1*1*1*1*1*3*3*1*1*1*1*1*1*1*",
                "201010101010101010101010101010102",
                "*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*3*",
                "201010101030101010301010101010102",
                "*1*3*1*1*1*3*1*1*3*1*1*1*1*3*1*1*",
                "203010101010101010101010103010102",
                "*1*1*1*1*1*1*3*1*1*1*1*1*1*1*1*1*",
                "201010101010103010101010101010102",
                "*1*1*1*1*1*1*1*1*1*3*1*1*1*1*1*1*",
                "201010101010101010103010101010102",
                "*3*1*1*1*1*1*1*1*1*1*1*1*1*1*3*1*",
                "201010103010101010101010101010302",
                "*1*1*1*3*1*1*1*1*1*1*1*1*1*1*1*1*",
                "201010101010301010101010301010102",
                "*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*",
            ],
            30,
            7
        ]


def creer_objet(position, color):
    if color == "R":
        color = "red"
    elif color == "G":
        color = "green"
    elif color == "B":
        color = "blue"
    elif color == "Y":
        color = "yellow"
    return canvas.create_rectangle(58 + COTE * position[1], 58 + COTE * position[0], 70 + COTE * position[1], 70 + COTE * position[0], fill=color)


def success_or_not(info_bot_controlled):
    global success
    if info_bot_controlled[1] == objet[0] and objet[1] == bot_controlling and success == False:
        success = True
        canvas.unbind_all("<Key>")
        tkinter.messagebox.showinfo("success", "SUccess unlocked")


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
    global liste
    bot_create = canvas.create_oval(48 + COTE * position[1], 48 + COTE * position[0], 80 + COTE * position[1], 80 + COTE * position[0], fill=color)
    if color == "red":
        color = "R"
    elif color == "green":
        color = "G"
    elif color == "blue":
        color = "B"
    elif color == "yellow":
        color = "Y"
    liste[position[0]*2+1][position[1]*2+1] = color
    return bot_create


def renouveler_position_dans_liste():

    global liste
    if bot_controlling == 'R':
        global info_bot_red
        x, y = info_bot_red[0]
        info_bot_red = calculer_position(info_bot_red[1][0], info_bot_red[1][1]) + [info_bot_red[-1]]
        liste[info_bot_red[0][0]][info_bot_red[0][1]], liste[x][y] = liste[x][y], 0
        return info_bot_red

    if bot_controlling == 'G':
        global info_bot_green
        x, y = info_bot_green[0]
        info_bot_green = calculer_position(info_bot_green[1][0], info_bot_green[1][1]) + [info_bot_green[-1]]
        liste[info_bot_green[0][0]][info_bot_green[0][1]], liste[x][y] = liste[x][y], 0
        return info_bot_green

    if bot_controlling == 'B':
        global info_bot_blue
        x, y = info_bot_blue[0]
        info_bot_blue = calculer_position(info_bot_blue[1][0], info_bot_blue[1][1]) + [info_bot_blue[-1]]
        liste[info_bot_blue[0][0]][info_bot_blue[0][1]], liste[x][y] = liste[x][y], 0
        return info_bot_blue
    
    if bot_controlling == 'Y':
        global info_bot_yellow
        x, y = info_bot_yellow[0]
        info_bot_yellow = calculer_position(info_bot_yellow[1][0], info_bot_yellow[1][1]) + [info_bot_yellow[-1]]
        liste[info_bot_yellow[0][0]][info_bot_yellow[0][1]], liste[x][y] = liste[x][y], 0
        return info_bot_yellow
    

def deplacement(event):
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow, bot_controlling, liste_obstacles
    key =  event.keysym

    if key == "Up":
        if bot_controlling == "R":
            info_bot_red = mouvement_up(bot_red, info_bot_red)
            success_or_not(info_bot_red)
        if bot_controlling == "G":
            info_bot_green = mouvement_up(bot_green, info_bot_green)
            success_or_not(info_bot_green)
        if bot_controlling == "B":
            info_bot_blue = mouvement_up(bot_blue, info_bot_blue)
            success_or_not(info_bot_blue)
        if bot_controlling == "Y":
            info_bot_yellow = mouvement_up(bot_yellow, info_bot_yellow)
            success_or_not(info_bot_yellow)

    elif key == "Down":
        if bot_controlling == "R":
            info_bot_red = mouvement_down(bot_red, info_bot_red)
            success_or_not(info_bot_red)
        if bot_controlling == "G":
            info_bot_green = mouvement_down(bot_green, info_bot_green)
            success_or_not(info_bot_green)
        if bot_controlling == "B":
            info_bot_blue = mouvement_down(bot_blue, info_bot_blue)
            success_or_not(info_bot_blue)
        if bot_controlling == "Y":
            info_bot_yellow = mouvement_down(bot_yellow, info_bot_yellow)
            success_or_not(info_bot_yellow)

    elif key == "Right":
        if bot_controlling == "R":
            info_bot_red = mouvement_right(bot_red, info_bot_red)
            success_or_not(info_bot_red)
        if bot_controlling == "G":
            info_bot_green = mouvement_right(bot_green, info_bot_green)
            success_or_not(info_bot_green)
        if bot_controlling == "B":
            info_bot_blue = mouvement_right(bot_blue, info_bot_blue)
            success_or_not(info_bot_blue)
        if bot_controlling == "Y":
            info_bot_yellow = mouvement_right(bot_yellow, info_bot_yellow)
            success_or_not(info_bot_yellow)

    elif key == "Left":
        if bot_controlling == "R":
            info_bot_red = mouvement_left(bot_red, info_bot_red)
            success_or_not(info_bot_red)
        if bot_controlling == "G":
            info_bot_green = mouvement_left(bot_green, info_bot_green)
            success_or_not(info_bot_green)
        if bot_controlling == "B":
            info_bot_blue = mouvement_left(bot_blue, info_bot_blue)
            success_or_not(info_bot_blue)
        if bot_controlling == "Y":
            info_bot_yellow = mouvement_left(bot_yellow, info_bot_yellow)
            success_or_not(info_bot_yellow)

    elif key == "g":
        change_bot_controlling("G")
    elif key == "r":
        change_bot_controlling("R")
    elif key == 'b':
        change_bot_controlling("B")
    elif key == 'y':
        change_bot_controlling("Y")


def change_bot_controlling(color_abrev):
    global liste_obstacles, bot_controlling
    bot_controlling = color_abrev
    liste_obstacles = ["2", "3", "R", "B", "Y", "G"]
    liste_obstacles.remove(color_abrev)


def map_enregistrement():
    try:
        with open(ficher_enregistrement_et_chargement, "w") as f:
            f.write(" ".join([str(element) for element in list(info_bot_red[1])]) + "\n")
            f.write(" ".join([str(element) for element in list(info_bot_green[1])]) + "\n")
            f.write(" ".join([str(element) for element in list(info_bot_blue[1])]) + "\n")
            f.write(" ".join([str(element) for element in list(info_bot_yellow[1])]) + "\n")
            f.write(" ".join([str(element) for element in list(objet[0])]) + "\n")
            f.write(objet[1] + "\n")
            for line in map_initial[5]:
                f.write(line + "\n")
    except:
        tkinter.messagebox.showerror("error", "Le map ne peut pas être enregistrer")
    else:
        tkinter.messagebox.showinfo("success", "Le map est enregistré")


def charger_map_depuis_un_fichier():
    global charger
    charger = True
    charger_map()
    charger = False

def recommencer():
    root.destroy()
    main()

def clique_du_souris(event):
    global charger
    if (366 < event.x < 468 and 370 < event.y < 464 or
        370 < event.x < 464 and 366 < event.y < 468):
        recommencer()
    elif 830 < event.x < 925 and 340 < event.y < 410:
        map_enregistrement()
    elif 947 < event.x < 1043 and 340 < event.y < 410:
        charger_map_depuis_un_fichier()
    elif 41 < event.x < 793 or 41 < event.x < 793:
        x, y = event.y//47-1, event.x//47-1
        if x == info_bot_red[1][0] and y == info_bot_red[1][1]:
            change_bot_controlling("R")
        elif x == info_bot_green[1][0] and y == info_bot_green[1][1]:
            change_bot_controlling("G")
        elif x == info_bot_blue[1][0] and y == info_bot_blue[1][1]:
            change_bot_controlling("B")
        elif x == info_bot_yellow[1][0] and y == info_bot_yellow[1][1]:
            change_bot_controlling("Y")


def mouvement_up(bot_controlled, info_bot_controlled):
    global success
    canvas.move(bot_controlled, 0, -info_bot_controlled[2][0] * 47)

    info_bot_controlled[1] = (info_bot_controlled[1][0]- info_bot_controlled[2][0], info_bot_controlled[1][1])
    if info_bot_controlled[2][0] != 0:
        info_bot_controlled = renouveler_position_dans_liste()
    return info_bot_controlled


def mouvement_down(bot_controlled, info_bot_controlled):
    canvas.move(bot_controlled, 0, info_bot_controlled[2][1] * 47)
    info_bot_controlled[1] = (info_bot_controlled[1][0] + info_bot_controlled[2][1], info_bot_controlled[1][1])

    if info_bot_controlled[2][1] != 0:
        info_bot_controlled = renouveler_position_dans_liste()
    return info_bot_controlled


def mouvement_left(bot_controlled, info_bot_controlled):
    canvas.move(bot_controlled, -info_bot_controlled[2][2] * 47, 0)
    info_bot_controlled[1] = (info_bot_controlled[1][0], info_bot_controlled[1][1] - info_bot_controlled[2][2])

    if info_bot_controlled[2][2] != 0:
        info_bot_controlled = renouveler_position_dans_liste()
    return info_bot_controlled


def mouvement_right(bot_controlled, info_bot_controlled):
    canvas.move(bot_controlled, info_bot_controlled[2][3] * 47, 0)
    info_bot_controlled[1] = (info_bot_controlled[1][0], info_bot_controlled[1][1] + info_bot_controlled[2][3])

    if info_bot_controlled[2][3] != 0:
        info_bot_controlled = renouveler_position_dans_liste()
    return info_bot_controlled


def charger_bot_et_objet_et_liste():
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow
    global bot_red, bot_green, bot_blue, bot_yellow
    global objet, liste
    
    liste = []
    for element in map_initial[5]:
        liste.append(list(element))

    info_bot_red = calculer_position(*map_initial[0]) + ["red"]
    info_bot_green = calculer_position(*map_initial[1]) + ["green"]
    info_bot_blue = calculer_position(*map_initial[2]) + ["blue"]
    info_bot_yellow = calculer_position(*map_initial[3]) + ["green"]

    bot_red = create_rectangle_en_fonction_de_position(info_bot_red[1], "red")
    bot_green = create_rectangle_en_fonction_de_position(info_bot_green[1], "green")
    bot_blue = create_rectangle_en_fonction_de_position(info_bot_blue[1], "blue")
    bot_yellow = create_rectangle_en_fonction_de_position(info_bot_yellow[1], "yellow")

    objet = map_initial[4]
    creer_objet(*objet)


def interface_initial():

    canvas.create_rectangle(33, 33, 801, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)
    canvas.create_rectangle(41, 41, 793, 793, fill=COUL_FOND)
    quadrillage()

    canvas.create_rectangle(830, 33, 1160, 298, fill=COUL_FOND_3, outline=COUL_FOND_3)
    canvas.create_rectangle(830, 340, 925, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
    canvas.create_rectangle(947, 340, 1043, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
    canvas.create_rectangle(1065, 340, 1160, 410, fill=COUL_FOND_3, outline=COUL_FOND_3)
    canvas.create_rectangle(830, 441, 1160, 801, fill=COUL_FOND_3, outline=COUL_FOND_3)

    ##rond de couleur
    canvas.create_oval(864, 717, 914, 767, fill='green')
    canvas.create_oval(864, 647, 914, 697, fill='blue')
    canvas.create_oval(1001, 717, 1051, 767, fill='yellow')
    canvas.create_oval(1001, 647, 1051, 697, fill='red')

    ##Lettres
    canvas.create_text(889, 742, fill='white', text='G',font='ArcadeClassic 30')
    canvas.create_text(889, 672, fill='white', text='B',font='ArcadeClassic 30')
    canvas.create_text(1026, 742, fill='#9FAB18', text='Y',font='ArcadeClassic 30')
    canvas.create_text(1026, 672, fill='white', text='R',font='ArcadeClassic 30')

    ##Texte des couleur
    canvas.create_text(949, 742, fill='white', text='Green',font='ArcadeClassic 17')
    canvas.create_text(949, 672, fill='white', text='Blue',font='ArcadeClassic 17')
    canvas.create_text(1086, 742, fill='white', text='Yellow',font='ArcadeClassic 17')
    canvas.create_text(1086, 672, fill='white', text='Red',font='ArcadeClassic 17')

    ##rectangle orange
    canvas.create_rectangle(1001, 57.5, 1125, 117.5, fill="orange", outline='yellow')
    canvas.create_rectangle(1001, 140, 1125, 200, fill='orange', outline='yellow')
    canvas.create_rectangle(1001, 222.5, 1125, 282.5, fill='orange', outline='yellow')

    ##Instruction
    canvas.create_text(940, 595, fill='white', text='SWITCH ROBOT',font='ArcadeClassic 20')
    canvas.create_text(935, 470, fill='white', text='HOW TO MOVE',font='ArcadeClassic 20')
    #record
    canvas.create_text(915, 85, fill='white', text='RECORD:',font='ArcadeClassic 20')
    canvas.create_text(1062.5, 85, fill='black', text='NONE',font='ArcadeClassic 30')
    #score
    canvas.create_text(920, 167.5, fill='white', text='SCORE:',font='ArcadeClassic 20')
    canvas.create_text(1062.5, 167.5, fill='black', text='NONE',font='ArcadeClassic 30')
    #move
    canvas.create_text(925, 250, fill='white', text='MOVE:',font='ArcadeClassic 20')
    canvas.create_text(1062.5, 250, fill='black', text='NONE',font='ArcadeClassic 30')


def main():
    global root, canvas
    root = tk.Tk()
    if not charger:
        charger_map()
    change_bot_controlling(bot_controlling)
    root.title('Robot Ricochet')
    root.geometry(f"{LARGEUR+10}x{HAUTEUR+10}")
    root.configure(bg=COUL_FOND_2)
    root.resizable(False, False)

    canvas = tk.Canvas(height=HAUTEUR, width=LARGEUR, bg=COUL_FOND_2)
    canvas.grid()
    interface_initial()
    charger_bot_et_objet_et_liste()
    dessiner_obstacles()
    
    canvas.bind_all("<Key>", deplacement)
    canvas.bind('<1>', clique_du_souris)

    root.mainloop()


main()