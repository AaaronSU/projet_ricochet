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

# Variables
LARGEUR = 1194
HAUTEUR = 834
COUL_FOND = "#ddd0b6"
COUL_FOND_2 = "#1b1b1b"
COUL_FOND_3 = "#292929"
COUL_QUADR = "#99958d"
dict_color = {"R": "red", "G": "green", "B": "blue", "Y": "yellow"}
ficher_enregistrement_et_chargement = "map.txt"
bot_controlling = "B"
charger = False
success = False
COTE = 47


def affichage_bot_controlling():
    """changement d'affichage de couleur en fonction du robot en control"""
    canvas.itemconfigure(nom_bot, fill=dict_color[bot_controlling],
                         outline=dict_color[bot_controlling])


def affichage_score_et_record():
    """affiche le score et le record du jeu"""
    canvas.itemconfigure(score_panel, text=score)
    canvas.itemconfigure(record_panel, text=record)


def affichage_image():
    """Ajoute les images dans l'interface graphique"""
    # Image
    global update_image, save_image, reload_image, retourne_image
    global up_arrow, down_arrow, left_arrow, right_arrow

    try:
        update_image = tk.PhotoImage(file='./img/update.png')
        canvas.create_image(417, 417, image=update_image)

        save_image = tk.PhotoImage(file='./img/save.png')
        canvas.create_image(877, 375, image=save_image)

        retourne_image = tk.PhotoImage(file='./img/retourne.png')
        canvas.create_image(997, 377, image=retourne_image)

        reload_image = tk.PhotoImage(file='./img/reload.png')
        canvas.create_image(1115, 375, image=reload_image)

        left_arrow = tk.PhotoImage(file='./img/left_arrow.png')
        canvas.create_image(915, 545, image=left_arrow)

        up_arrow = tk.PhotoImage(file='./img/up_arrow.png')
        canvas.create_image(971, 545, image=up_arrow)

        down_arrow = tk.PhotoImage(file='./img/down_arrow.png')
        canvas.create_image(1024, 545, image=down_arrow)

        right_arrow = tk.PhotoImage(file='./img/right_arrow.png')
        canvas.create_image(1080, 545, image=right_arrow)
    except:
        pass


def calculer_position(x, y):
    """Calcul la position d'un robot en fonction de sa position sur la map,
    et retourne une liste qui affiche en premier élément la position du robot
    dans la liste de la map, en deuxième élément la position
    du robot sur la map, et en dernier élément les
    déplacements possible du robot"""
    return [(x*2+1, y*2+1), (x, y), deplacement_possible(x*2+1, y*2+1)]


def change_bot_controlling(color_abrev):
    """Fonction permettant de passer du control d'un robot à un autre
    et change la liste d'obstacle en fonction du robot contrôlé"""
    global liste_obstacles, bot_controlling
    bot_controlling = color_abrev
    liste_obstacles = ["2", "3", "R", "B", "Y", "G"]
    liste_obstacles.remove(color_abrev)


def change_bot_controlling_avec_des_cliques(event):
    """Change le robot en control en fonction du clique du souris"""
    x, y = event.y//47-1, event.x//47-1
    bot_controlling_tempo = bot_controlling
    recalcul_de_position()
    change_bot_controlling(bot_controlling_tempo)
    if x == info_bot_red[1][0] and y == info_bot_red[1][1]:
        change_bot_controlling("R")
    elif x == info_bot_green[1][0] and y == info_bot_green[1][1]:
        change_bot_controlling("G")
    elif x == info_bot_blue[1][0] and y == info_bot_blue[1][1]:
        change_bot_controlling("B")
    elif x == info_bot_yellow[1][0] and y == info_bot_yellow[1][1]:
        change_bot_controlling("Y")
    affichage_bot_controlling()


def change_record():
    """changement de record en fonction du
    score du jeu à la fin de la partie"""
    global record
    record = score if record == "N" or record > score else record
    canvas.itemconfigure(record_panel, text=record)


def charger_bot_et_objet_et_liste():
    """Charge dans une liste la map,
    puis charge et crée les robots ainsi que les cibles"""
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow
    global bot_red, bot_green, bot_blue, bot_yellow
    global objet, liste, bot_controlling
    global record, score

    liste = []
    for element in map_initial[5]:
        liste.append(list(element))

    info_bot_red = calculer_position(*map_initial[0]) + ["red"]
    info_bot_green = calculer_position(*map_initial[1]) + ["green"]
    info_bot_blue = calculer_position(*map_initial[2]) + ["blue"]
    info_bot_yellow = calculer_position(*map_initial[3]) + ["yellow"]

    bot_red = create_robot_en_fonction_de_position(info_bot_red[1], "red")
    bot_green = (create_robot_en_fonction_de_position
                 (info_bot_green[1], "green"))
    bot_blue = create_robot_en_fonction_de_position(info_bot_blue[1], "blue")
    bot_yellow = (create_robot_en_fonction_de_position
                  (info_bot_yellow[1], "yellow"))
    bot_controlling_tempo = bot_controlling
    recalcul_de_position()
    change_bot_controlling(bot_controlling_tempo)

    objet = map_initial[4]
    creer_objet(*objet)
    if success:
        map_initial[7] = 0
        if map_initial[6] == "N" or record < map_initial[6]:
            map_initial[6] = record
    record = map_initial[6]
    score = map_initial[7]


def charger_map():
    """Charge la dernière sauvegarde du jeu effectué par l'utilisateur,
    si pas de sauvegarde charge le terrain de jeu prédéfini"""
    global map_initial
    if charger:
        try:
            with open(ficher_enregistrement_et_chargement, "r") as f:
                map_initial = []
                nombre_ligne = 0
                for line in f.readlines():
                    if nombre_ligne < 5:
                        sous_map_initial = line[:-1].split(" ")
                        sous_map_initial = [int(element) for
                                            element in sous_map_initial]
                        map_initial.append(sous_map_initial)
                    elif nombre_ligne == 4:
                        sous_map_initial = line[:-1].split(" ")
                        sous_map_initial = [int(element) for
                                            element in sous_map_initial]
                        map_initial.append(sous_map_initial)
                    elif nombre_ligne == 5:
                        map_initial[-1].append(line[:-1])
                        map_initial.append([])
                    elif 5 < nombre_ligne < 39:
                        map_initial[-1].append(line[:-1])
                    elif nombre_ligne == 39:
                        record = "N" if line[:-1] == "N" else int(line[:-1])
                        map_initial.append(record)
                    else:
                        map_initial.append(int(line[:-1]))
                    nombre_ligne += 1
                map_initial[4] = ((map_initial[4][0], map_initial[4][1]),
                                  map_initial[4][2])
        except:
            tkinter.messagebox.showerror("error",
                                         "Le fichier du chargement"
                                         " n'existe pas")
        else:
            tkinter.messagebox.showinfo("sucess", "Le map est chargé")
            root.destroy()
            main()
    else:
        map_initial = [
            (3, 15),  # red
            (1, 9),  # green
            (9, 5),  # blue
            (13, 5),  # yellow
            ((6, 1), "Y"),
            [
                "*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*",
                "201010103010101010103010101010102",
                "*1*1*1*1*1*1*1*1*1*1*1*1*3*1*1*1*",
                "201010101010101010101010301010102",
                "*1*1*1*1*1*3*1*1*1*1*1*1*1*1*1*3*",
                "201010101010301010101010101010102",
                "*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*",
                "201010101010101010301010101010102",
                "*1*1*3*1*1*1*1*1*1*3*1*1*1*1*1*1*",
                "201010301010101010101010101010302",
                "*3*1*1*1*1*1*1*1*1*1*3*1*1*1*3*1*",
                "201010101010103010101030101010102",
                "*1*3*1*1*1*1*1*3*1*1*1*1*1*1*1*1*",
                "203010101010101010101010101010102",
                "*1*1*1*1*1*1*1*3*3*1*1*1*1*1*1*1*",
                "201010101010103030301010101010102",
                "*1*1*1*1*1*1*1*3*3*1*1*1*1*1*1*1*",
                "201010101010303030301010101010102",
                "*1*1*1*1*1*3*1*3*3*1*1*1*3*1*1*1*",
                "201010101010101010101010301010102",
                "*1*1*3*1*1*1*1*2*2*1*1*1*1*1*1*3*",
                "201030101010101010101030101010102",
                "*1*1*1*1*1*1*1*1*1*1*3*1*1*1*1*1*",
                "201010101010101010101010101010102",
                "*3*1*1*1*1*1*1*1*1*1*1*1*1*1*3*1*",
                "201010101010101010101010101010302",
                "*1*1*1*1*3*1*1*1*1*1*1*1*1*1*1*1*",
                "201010103010101010101010101010102",
                "*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*1*",
                "201010101010301010101030101010102",
                "*1*1*1*1*1*1*3*1*1*1*1*3*1*1*1*1*",
                "201010101030101010101010101030102",
                "*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*",
            ],
            "N",
            0
        ]


def charger_map_depuis_un_fichier():
    """Charger la dernière sauvegarde du jeu"""
    global charger
    charger = True
    charger_map()
    charger = False


def clique_du_souris(event):
    """En fonction de l'endroit ou se situe le clic de l'utilisateur,
    soit la partie recommence, soit une sauvegarde s'effectue,
    soit une reprise de sauvegarde s'effectue,
    soit l'utilisateur controle un robot d'une
    autre couleur que celui qu'il est en train de contrôler
    si il clique sur un autre"""
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow
    global charger
    if 366 < event.x < 468 and 370 < event.y < 464 or \
        370 < event.x < 464 and \
            366 < event.y < 468:
            recommencer()
    elif 830 < event.x < 925 and 340 < event.y < 410:
        map_enregistrement()
    elif 947 < event.x < 1043 and 340 < event.y < 410:
        if len(list_mouvement) != 0:
            retourner_a_l_arriere()
    elif 41 < event.x < 793 and 41 < event.y < 793:
        change_bot_controlling_avec_des_cliques(event)
    elif 1065 < event.x < 1160 and 340 < event.y < 410:
        charger_map_depuis_un_fichier()


def create_robot_en_fonction_de_position(position, color):
    """Crée le robot en fonction de la position et de la couleur qu'on lui attribue
    et renouvelle l'élément dans la liste en fonction de sa couleur"""
    global liste
    bot_create = canvas.create_oval(48 + COTE * position[1],
                                    48 + COTE * position[0],
                                    80 + COTE * position[1],
                                    80 + COTE * position[0],
                                    fill=color)
    liste[position[0]*2+1][position[1]*2+1] = \
        list(dict_color.keys())[list(dict_color.values()).index(color)]
    return bot_create


def creer_objet(position, color):
    """Fait apparaître la cible"""
    return canvas.create_rectangle(58 + COTE * position[1],
                                   58 + COTE * position[0],
                                   70 + COTE * position[1],
                                   70 + COTE * position[0],
                                   fill=dict_color[color])


def deplacement(event):
    """Fonction permettant à l'utilisateur de choisir le
    robot qu'il souhaite contrôler, et de les contrôler
    grâce aux touches du clavier"""
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow
    key = event.keysym

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

    elif key == "g" or "r" or "b" or "y":
        recalcul_de_position()
        if key == "g":
            change_bot_controlling("G")
        elif key == "r":
            change_bot_controlling("R")
        elif key == "b":
            change_bot_controlling("B")
        elif key == "y":
            change_bot_controlling("Y")

    if key == "z":
        if len(list_mouvement) != 0:
            retourner_a_l_arriere()
        change_bot_controlling(bot_controlling)

    affichage_bot_controlling()


def deplacement_possible(x, y):
    """Calcul les déplacements possible d'un robot en fonction de sa position
    sur la map"""
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


def dessiner_obstacles():
    """Rend les obstacles visibles"""
    for i in range(len(liste)):
        if i == 0 or i == 32:
            pass
        elif i % 2 == 1:
            for j in range(1, 32):
                if liste[i][j] == "3":
                    canvas.create_rectangle(
                        37 + j // 2 * 47,
                        41 + i // 2 * 47,
                        45 + j // 2 * 47,
                        41 + (i // 2 + 1) * 47,
                        fill='black'
                    )
        else:
            for j in range(1, 32):
                if liste[i][j] == "3":
                    canvas.create_rectangle(
                        41 + j//2 * 47,
                        37 + i//2 * 47,
                        41 + (j//2 + 1) * 47,
                        45 + i//2 * 47,
                        fill='black'
                    )


def interface_initial():
    """Creation de l'interface du jeu,
    le terrain, les boutons, et les textes"""
    global nom_bot, score_panel, record_panel
    round_rectangle(33, 33, 801, 801, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)
    round_rectangle(41, 41, 793, 793, radius=20, fill=COUL_FOND)
    quadrillage()

    round_rectangle(830, 33, 1160, 298, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)
    round_rectangle(830, 340, 925, 410, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)
    round_rectangle(947, 340, 1043, 410, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)
    round_rectangle(1065, 340, 1160, 410, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)
    round_rectangle(830, 441, 1160, 801, radius=20,
                    fill=COUL_FOND_3, outline=COUL_FOND_3)

    # carre noir du milieu
    canvas.create_rectangle(370, 370, 464, 464, fill="black")

    # rond de couleur
    canvas.create_oval(864, 718, 914, 767, fill='#008017', outline=COUL_FOND_3)
    canvas.create_oval(864, 647, 914, 697, fill='#5821FA', outline=COUL_FOND_3)
    canvas.create_oval(1001, 717, 1051, 767,
                       fill='#FBFF48', outline=COUL_FOND_3)
    canvas.create_oval(1001, 647, 1051, 697,
                       fill='#FF101E', outline=COUL_FOND_3)

    # Lettres
    canvas.create_text(889, 742, fill='#BDE1A6',
                       text='G', font='ArcadeClassic 17')
    canvas.create_text(889, 672, fill='#ACD3DF',
                       text='B', font='ArcadeClassic 17')
    canvas.create_text(1026, 742, fill='#9FAB18',
                       text='Y', font='ArcadeClassic 17')
    canvas.create_text(1026, 672, fill='#E3D8D8',
                       text='R', font='ArcadeClassic 17')

    # Texte des couleur
    canvas.create_text(949, 742, fill='#808080',
                       text='GREEN', font='ArcadeClassic 12')
    canvas.create_text(949, 672, fill='#808080',
                       text='BLUE', font='ArcadeClassic 12')
    canvas.create_text(1095, 742, fill='#808080',
                       text='YELLOW', font='ArcadeClassic 12')
    canvas.create_text(1086, 672, fill='#808080',
                       text='RED', font='ArcadeClassic 12')

    # rectangle orange
    round_rectangle(1000, 55, 1130, 115, fill="#FFA31A", outline="#FFA31A")
    round_rectangle(1000, 134, 1130, 194, fill='#FFA31A', outline="#FFA31A")
    round_rectangle(1000, 213, 1130, 273, fill='#FFA31A', outline="#FFA31A")

    # Instruction
    canvas.create_text(955, 610, fill='#FFFFFF',
                       text='SWITCH ROBOT', font='ArcadeClassic 20')
    canvas.create_text(950, 480, fill='#FFFFFF',
                       text='HOW TO MOVE', font='ArcadeClassic 20')
    # record
    canvas.create_text(915, 87, fill='#FFFFFF',
                       text='RECORD :', font='ArcadeClassic 18')
    record_panel = canvas.create_text(1065, 85, fill='black',
                                      text="0",
                                      font='ArcadeClassic 25')
    # score
    canvas.create_text(920, 165, fill='#FFFFFF',
                       text='SCORE :', font='ArcadeClassic 18')
    score_panel = canvas.create_text(1065, 165, fill='black',
                                     text="0", font='ArcadeClassic 25')
    # Bot
    canvas.create_text(920, 245, fill='#FFFFFF',
                       text='BOT :', font='ArcadeClassic 18')
    nom_bot = canvas.create_oval(1047, 227, 1082, 262)


def map_enregistrement():
    """Enregistre la partie de jeu en cours dans un fichier txt"""
    try:
        with open(ficher_enregistrement_et_chargement, "w") as f:
            f.write(" ".join([str(element) for
                    element in list(info_bot_red[1])]) + "\n")
            f.write(" ".join([str(element) for
                    element in list(info_bot_green[1])]) + "\n")
            f.write(" ".join([str(element) for
                    element in list(info_bot_blue[1])]) + "\n")
            f.write(" ".join([str(element) for
                    element in list(info_bot_yellow[1])]) + "\n")
            f.write(" ".join([str(element) for
                    element in list(objet[0])]) + "\n")
            f.write(objet[1] + "\n")
            for line in map_initial[5]:
                f.write(line + "\n")
            f.write(str(record) + "\n")
            f.write(str(score) + "\n")
    except:
        tkinter.messagebox.showerror("error",
                                     "Le map ne peut pas"
                                     " être enregistrer")
    else:
        tkinter.messagebox.showinfo("success", "Le map est enregistré")


def mouvement_up(bot_controlled, info_bot_controlled):
    """fonction permettant le deplacement vers le haut d'un robot
    tant que le robot ne se situe pas juste en-dessous d'un obstacle"""
    global score, list_mouvement

    if info_bot_controlled[2][0] != 0:
        list_mouvement.append((info_bot_controlled[1], bot_controlling))
        canvas.move(bot_controlled, 0, -info_bot_controlled[2][0] * 47)
        info_bot_controlled[1] = (info_bot_controlled[1][0] -
                                  info_bot_controlled[2][0],
                                  info_bot_controlled[1][1])
        info_bot_controlled = renouveler_position_dans_liste()
        score += 1
    affichage_score_et_record()
    return info_bot_controlled


def mouvement_down(bot_controlled, info_bot_controlled):
    """fonction permettant le deplacement vers le bas d'un robot
    tant que le robot ne se situe pas juste au-dessus d'un obstacle"""
    global score, list_mouvement

    if info_bot_controlled[2][1] != 0:
        list_mouvement.append((info_bot_controlled[1], bot_controlling))
        canvas.move(bot_controlled, 0, info_bot_controlled[2][1] * 47)
        info_bot_controlled[1] = (info_bot_controlled[1][0] +
                                  info_bot_controlled[2][1],
                                  info_bot_controlled[1][1])
        info_bot_controlled = renouveler_position_dans_liste()
        score += 1
    affichage_score_et_record()
    return info_bot_controlled


def mouvement_left(bot_controlled, info_bot_controlled):
    """fonction permettant le deplacement vers la gauche d'un robot
    tant que le robot ne se situe pas juste à droite d'un obstacle"""
    global score, list_mouvement

    if info_bot_controlled[2][2] != 0:
        list_mouvement.append((info_bot_controlled[1], bot_controlling))
        canvas.move(bot_controlled, -info_bot_controlled[2][2] * 47, 0)
        info_bot_controlled[1] = (info_bot_controlled[1][0],
                                  info_bot_controlled[1][1] -
                                  info_bot_controlled[2][2])
        info_bot_controlled = renouveler_position_dans_liste()
        score += 1
    affichage_score_et_record()
    return info_bot_controlled


def mouvement_right(bot_controlled, info_bot_controlled):
    """fonction permettant le deplacement vers la droite d'un robot
    tant que le robot ne se situe pas juste à gauche d'un obstacle"""
    global score, list_mouvement

    if info_bot_controlled[2][3] != 0:
        list_mouvement.append((info_bot_controlled[1], bot_controlling))
        canvas.move(bot_controlled, info_bot_controlled[2][3] * 47, 0)
        info_bot_controlled[1] = (info_bot_controlled[1][0],
                                  info_bot_controlled[1][1] +
                                  info_bot_controlled[2][3])
        info_bot_controlled = renouveler_position_dans_liste()
        score += 1
    affichage_score_et_record()
    return info_bot_controlled


def success_or_not(info_bot_controlled):
    """Affiche un message quand le robot atteint
    la cible. Et redemande à l'utilisateur s'il
    souhaite rejouer"""
    global success
    if info_bot_controlled[1] == objet[0] and\
            objet[1] == bot_controlling and not success:
        success = True
        canvas.unbind_all("<Key>")
        change_record()
        tkinter.messagebox.showinfo("success",
                                    f"Success unlocked with {score} move")
        continue_game = tkinter.messagebox.askyesno("Continuer le jeu",
                                                    "Vous voulez continuer"
                                                    " à jouer")
        if continue_game:
            recommencer()


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


def recalcul_de_position():
    """Recalcul la position des robots en fonction de leurs positions"""
    global info_bot_red, info_bot_green, info_bot_blue, info_bot_yellow
    change_bot_controlling("R")
    info_bot_red = calculer_position(*info_bot_red[1]) + ["red"]
    change_bot_controlling("G")
    info_bot_green = calculer_position(*info_bot_green[1]) + ["green"]
    change_bot_controlling("B")
    info_bot_blue = calculer_position(*info_bot_blue[1]) + ["blue"]
    change_bot_controlling("Y")
    info_bot_yellow = calculer_position(*info_bot_yellow[1]) + ["yellow"]


def recommencer():
    """Fait recommencer une nouvelle partie où tout
    les robots reviennent à leurs positions de départ"""
    root.destroy()
    main()


def renouveler_position_dans_liste():
    """Calcul la position du robot en cours de control
    afin de pouvoir limiter leurs déplacement"""
    global liste
    if bot_controlling == 'R':
        global info_bot_red
        x, y = info_bot_red[0]

        info_bot_red = calculer_position(info_bot_red[1][0],
                                         info_bot_red[1][1]) +\
            [info_bot_red[-1]]

        liste[info_bot_red[0][0]][info_bot_red[0][1]],\
            liste[x][y] = liste[x][y], 0

        return info_bot_red

    if bot_controlling == 'G':
        global info_bot_green
        x, y = info_bot_green[0]

        info_bot_green = calculer_position(info_bot_green[1][0],
                                           info_bot_green[1][1]) +\
            [info_bot_green[-1]]

        liste[info_bot_green[0][0]][info_bot_green[0][1]],\
            liste[x][y] = liste[x][y], 0

        return info_bot_green

    if bot_controlling == 'B':
        global info_bot_blue
        x, y = info_bot_blue[0]

        info_bot_blue = calculer_position(info_bot_blue[1][0],
                                          info_bot_blue[1][1]) +\
            [info_bot_blue[-1]]

        liste[info_bot_blue[0][0]][info_bot_blue[0][1]],\
            liste[x][y] = liste[x][y], 0

        return info_bot_blue

    if bot_controlling == 'Y':
        global info_bot_yellow
        x, y = info_bot_yellow[0]

        info_bot_yellow = calculer_position(info_bot_yellow[1][0],
                                            info_bot_yellow[1][1]) +\
            [info_bot_yellow[-1]]

        liste[info_bot_yellow[0][0]][info_bot_yellow[0][1]],\
            liste[x][y] = liste[x][y], 0

        return info_bot_yellow


def retourner_a_l_arriere():
    """Fonction undo"""
    global info_bot_red, info_bot_blue, info_bot_green, info_bot_yellow
    global liste, score

    dict_robot = {
            "R": (bot_red, info_bot_red),
            "B": (bot_blue, info_bot_blue),
            "G": (bot_green, info_bot_green),
            "Y": (bot_yellow, info_bot_yellow)
        }
    bot, info_bot = dict_robot[list_mouvement[-1][1]]
    canvas.move(bot, (list_mouvement[-1][0][1] - info_bot[1][1]) * 47,
                (list_mouvement[-1][0][0] - info_bot[1][0]) * 47)
    liste[list_mouvement[-1][0][0] * 2 + 1][list_mouvement[-1][0][1]*2+1] =\
        list_mouvement[-1][1]
    liste[info_bot[1][0] * 2 + 1][info_bot[1][1] * 2 + 1] = 0

    if list_mouvement[-1][1] == "R":
        info_bot_red = calculer_position(*list_mouvement[-1][0]) + ["red"]
    elif list_mouvement[-1][1] == "B":
        info_bot_blue = calculer_position(*list_mouvement[-1][0]) + ["blue"]
    elif list_mouvement[-1][1] == "G":
        info_bot_green = calculer_position(*list_mouvement[-1][0]) + ["green"]
    elif list_mouvement[-1][1] == "Y":
        info_bot_yellow = calculer_position(*list_mouvement[-1][0]) +\
            ["yellow"]
    change_bot_controlling(list_mouvement[-1][1])
    del list_mouvement[-1]
    score -= 1
    affichage_score_et_record()


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    """crée les polygones avec des angles"""
    # un programme venant du site starkoverflow
    # lien : https://stackoverflow.com/questions/44099594/how-to-make-
    #        a-tkinter-canvas-rectangle-with-rounded-corners?rq=1

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def main():
    """Programme principale"""
    global root, canvas, success
    global list_mouvement
    root = tk.Tk()
    if not charger:
        charger_map()
    change_bot_controlling(bot_controlling)
    root.title('Robot Ricochet')
    root.config(bg=COUL_FOND_2)
    root.resizable(False, False)
    list_mouvement = []

    canvas = tk.Canvas(height=HAUTEUR, width=LARGEUR, bg=COUL_FOND_2)
    canvas.grid()
    interface_initial()
    charger_bot_et_objet_et_liste()
    dessiner_obstacles()
    affichage_image()
    affichage_bot_controlling()
    affichage_score_et_record()

    success = False

    canvas.bind_all("<Key>", deplacement)
    canvas.bind('<1>', clique_du_souris)

    root.mainloop()


main()
