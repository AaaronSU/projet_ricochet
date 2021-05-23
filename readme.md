![](img/exemple_de_terrain.png)


## Description du jeu Robot Ricochet

Ce jeu est composé d’une grille carré de taille 16x16. Deux cases voisines de la grille peuvent être séparées par un mur vertical ou horizontal. De plus, on considère qu’un mur encadre le bord extérieur de la grille. Quatre robots de couleur rouge, jaune, vert et bleu sont placés sur des cases de la grille. Une case de la grille est de la couleur d’un des robots: il s’agit de la cible qui doit être atteinte par le robot de cette couleur afin de résoudre le jeu.

Les règles de déplacement des robots sont les suivantes:

- [X] ils ne se déplacent qu’en ligne droite, horizontale ou verticale

- [X] ils ne s’arrêtent que quand ils rencontrent un obstacle qui est soit un mur soit un autre robot

- [X] cela compte pour un déplacement de robot, indépendamment du nombre de cases parcourues

- [X] un seul robot se déplace à chaque fois

Un objectif secondaire du jeu est de le résoudre en faisant le moins de déplacements possible.

## Interface graphique

Pour l’interface graphique, les principales caractéristiques attendues sont:

- [X] les quatre robots sont représentés par des cercles de couleur rouge, jaune, vert et bleu

- [X] la cible est représentée par un carré de la couleur d’un robot

- [X] les quatre cases du milieu sont entourées de murs, et non accessibles par les robots; par ailleurs, un clic sur une de ces cases redémarre la partie au début

- [X] quand on clique sur un robot, on peut ensuite le déplacer avec les flèches du clavier

- [X] quand on clique sur les touches, on peut changer le robot

- [X] un compteur affiche le nombre de déplacements effectués

- [X] quand la cible est atteinte par le robot de la bonne couleur, un message affiche que le jeu est résolu et indique le score (le nombre de déplacements de robots)


## Fonctionnalités avancées

En plus de la programmation du jeu, vous programmerez les fonctionnalités suivantes:

- [X] pouvoir sauvegarder une partie en cours, et la recharger ensuite

- [X] pouvoir sauvegarder le score d’une partie (le nombre de déplacements de robots), et pouvoir afficher les meilleurs scores

- [X] pouvoir revenir en arrière en annulant les derniers déplacements

- [ ] pouvoir éditer un plateau de jeu: placement des robots, de la cible, et des murs, choix de la couleur de la cible


## Défit Actuel

- Explication du jeu et du programme(readme)
- Convention PEP8 à respecter
- Possibilité de rajouter les fonctionnalités avancées
    - pouvoir éditer un plateau de jeu : placement des robots, de la cible, et des murs, choix de la couleur de la cible


![](img/robot_ricochet_UI.png)*


Quatres robots de couleurs bleu, vert, jaune et rouge sont mis à ta disposition. Le but du jeu est d'arriver à atteindre la case de la grille qui est coloré avec le robot correspond à cette couleur.
Pour cela, tu peux utiliser toutes les options qui te sont permises :
    - déplacement, pour te déplacer utilises simplement les flèches de ton clavier(les mouvements sont décrit sur le plateau de jeu)
    - changement de robot, il te faut cliquer sur le robot que tu souhaites déplacer ou bien appuyer sur la lettre correspondant au robot
    -score, à chaque déplacement le score augmente de 1
    - record, il correspond au meilleur score que vous ayé fait 
    - retour en arrière, cette commande te permet de revenir en arrière, le score diminue donc de 1 et elle correspond à la fléche pointé vers la gauche
    - enregistrement de la partie en cours, *********
    -récupération de la partie enregistré, en utilisant l'option de récupération cela te permet de retrouver la partie que tu avais auparavant joué
    - nouvelle partie, cela correspond à l'option situé au centre du plateau de jeu et elle te permet de recommencer une partie
