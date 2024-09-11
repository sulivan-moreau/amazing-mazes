import random

def generation_matrice():
    mur_bloquer = "@"
    mur = "#"
    chemin = "."
    entree = "E"
    sortie = "S"

    taille_mat = int(input("Taille de la matrice : "))
    taille_mat = (taille_mat * 2) + 1

    mat = [[mur for _ in range(taille_mat)] for _ in range(taille_mat)]

    for i in range(taille_mat):
        mat[0][i] = mur_bloquer
        mat[taille_mat - 1][i] = mur_bloquer
    for i in range(taille_mat):
        mat[i][0] = mur_bloquer
        mat[i][taille_mat - 1] = mur_bloquer

    mat[1][1] = entree
    
    sortie_x, sortie_y = taille_mat - 2, taille_mat - 2
    
    creer_chemin(mat, 1, 1)
    
    mat[sortie_x][sortie_y] = sortie

    for ligne in mat:
        print(" ".join(ligne))

    return mat

def voisin_valide(mat, x, y):
    taille_mat = len(mat)
    return 1 <= x < taille_mat - 1 and 1 <= y < taille_mat - 1 and mat[x][y] == "#"


def creer_chemin(mat, x, y):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if voisin_valide(mat, nx, ny):
            mat[x + dx // 2][y + dy // 2] = "."
            mat[nx][ny] = "."

            creer_chemin(mat, nx, ny)

def sauvegarde_fichier(mat):
    nom_fichier = input("Nom du fichier de sauvegarde : ")
    with open(nom_fichier + ".txt", "w") as fichier:
        for ligne in mat:
            fichier.write(" ".join(ligne) + "\n")

if __name__ == "__main__":
    mat = generation_matrice()
    sauvegarde_fichier(mat)