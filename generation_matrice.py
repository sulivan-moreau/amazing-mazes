def generation_matrice():
    mur = "#"
    chemin = "."
    entree = "E"
    sortie = "S"

    taille_mat = int(input("Taille de la matrice : "))
    taille_mat = (taille_mat * 2) + 1

    mat = [[mur for _ in range(taille_mat)] for _ in range(taille_mat)]
    
    
    for i in range(taille_mat):
        mat[0][i] = mur
        mat[taille_mat - 1][i] = mur

    for i in range(taille_mat):
        mat[i][0] = mur
        mat[i][taille_mat - 1] = mur

    
    mat[1][1] = entree
    mat[taille_mat - 2][taille_mat - 2] = sortie

   
    for ligne in mat:
        print(" ".join(ligne))

    return mat 
 
#def generation_labyrinthe():
    

def sauvegarde_fichier(mat):
    nom_fichier = input("Nom du fichier de sauvegarde : ")
    with open(nom_fichier + ".txt", "w") as fichier:
        for ligne in mat:
            fichier.write(" ".join(ligne) + "\n")
            
            