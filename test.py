import random

mur = "#"
chemin = "."


def initialiser_matrice(taille):
    return [[mur] * taille for _ in range(taille)]


def generer_labyrinthe(taille):
    matrice = initialiser_matrice(taille)
    matrice[0][0] = chemin
    matrice[taille - 1][taille - 1] = chemin

    generer_chemin(0, 0, matrice, taille)

    return matrice


def generer_chemin(x, y, matrice, taille):
    #  haut, bas, gauche, droite
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        print(directions)
        print(dx, dy)
        nx, ny = x + dx, y + dy
        if 0 <= nx < taille and 0 <= ny < taille and matrice[nx][ny] == mur:

            matrice[nx][ny] = chemin
            matrice[x + dx // 2][
                y + dy // 2
            ] = chemin  # Ouvrir un passage entre les deux
            print(x + dx // 2, y + dy // 2)

            generer_chemin(nx, ny, matrice, taille)


def afficher_labyrinthe(matrice):
    for ligne in matrice:
        print("".join(ligne))


taille_labyrinthe = int(input("Entrez la taille du labyrinthe: "))
labyrinthe = generer_labyrinthe(taille_labyrinthe)
afficher_labyrinthe(labyrinthe)
