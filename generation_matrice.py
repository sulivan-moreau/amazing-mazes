import random

def generation_matrice():
    mur_bloquer = "@"
    mur = "#"
    chemin = "."
    entree = "E"
    sortie = "S"

    taille_mat = int(input("Taille de la matrice : "))
    taille_mat = (taille_mat * 2) + 3  # Taille impaire pour un labyrinthe parfait

    # Initialiser la matrice avec des murs partout
    mat = [[mur for _ in range(taille_mat)] for _ in range(taille_mat)]

    # Placer les murs bloqués autour
    for i in range(taille_mat):
        mat[0][i] = mur_bloquer
        mat[taille_mat - 1][i] = mur_bloquer
    for i in range(taille_mat):
        mat[i][0] = mur_bloquer
        mat[i][taille_mat - 1] = mur_bloquer

    # Placer l'entrée
    mat[1][1] = entree
    
    sortie_x, sortie_y = taille_mat - 2, taille_mat - 2
    
    # Générer un labyrinthe parfait avec un chemin unique entre entrée et sortie
    creer_chemin(mat, 1, 1)

    # Placer la sortie à nouveau pour s'assurer qu'elle ne soit pas écrasée
    mat[sortie_x][sortie_y] = sortie

    # Afficher la matrice générée
    for ligne in mat:
        print(" ".join(ligne))

    return mat

def voisin_valide(mat, x, y):
    taille_mat = len(mat)
    # Vérifie que la cellule est dans la grille et n'a pas encore été visitée (reste un mur)
    return 1 <= x < taille_mat - 1 and 1 <= y < taille_mat - 1 and mat[x][y] == "#"


def creer_chemin(mat, x, y):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Déplacements possibles (de 2 cases à la fois)
    random.shuffle(directions)  # Mélanger les directions pour rendre le labyrinthe aléatoire

    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # Nouvelle position

        if voisin_valide(mat, nx, ny):
            # Creuser le chemin entre les deux cellules (supprimer les murs)
            mat[x + dx // 2][y + dy // 2] = "."  # Creuser entre les deux cases
            mat[nx][ny] = "."  # Marquer la nouvelle cellule comme un chemin

            # Continuer la génération à partir de cette nouvelle cellule
            creer_chemin(mat, nx, ny)

def sauvegarde_fichier(mat):
    nom_fichier = input("Nom du fichier de sauvegarde : ")
    with open(nom_fichier + ".txt", "w") as fichier:
        for ligne in mat:
            fichier.write(" ".join(ligne) + "\n")

if __name__ == "__main__":
    mat = generation_matrice()
    sauvegarde_fichier(mat)