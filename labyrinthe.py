import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def generation_matrice():
    mur = "#"
    entree = "E"
    sortie = "S"

    taille_mat = int(input("Taille de la matrice : "))
    taille_mat = (taille_mat * 2) + 1

    mat = [[mur for _ in range(taille_mat)] for _ in range(taille_mat)]

    for i in range(taille_mat):
        mat[0][i] = mat[taille_mat - 1][i] = mat[i][0] = mat[i][taille_mat - 1] = mur

    mat[1][1] = entree
    mat[taille_mat - 2][taille_mat - 2] = sortie

    generer_chemin_backtracking(mat, 1, 1)

    afficher_matrice(mat)

    return mat

def generer_chemin_backtracking(mat, x, y):
    pile = [(x, y)]
    while pile:
        x, y = pile[-1]
        voisins = obtenir_voisins(mat, x, y)
        if not voisins:
            pile.pop()
        else:
            nx, ny = random.choice(voisins)
            mat[nx][ny] = "."
            mat[(x + nx) // 2][(y + ny) // 2] = "."
            pile.append((nx, ny))

def obtenir_voisins(mat, x, y):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # droite, bas, gauche, haut
    voisins = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(mat) and 0 <= ny < len(mat) and mat[nx][ny] == "#":
            voisins.append((nx, ny))
    return voisins

def sauvegarde_fichier(mat):
    nom_fichier = input("Nom du fichier de sauvegarde : ")
    with open(nom_fichier + ".txt", "w") as fichier:
        for ligne in mat:
            fichier.write(" ".join(ligne) + "\n")

def afficher_matrice(mat):
    for ligne in mat:
        ligne_affichee = ""
        for cellule in ligne:
            if cellule == ".":
                ligne_affichee += Fore.BLUE + cellule + Style.RESET_ALL
            else:
                ligne_affichee += cellule
        print(ligne_affichee)

mat = generation_matrice()
sauvegarde_fichier(mat)
