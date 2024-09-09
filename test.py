taille_mat = int(input("Taille de la matrice : "))
nom_fichier = input("Fichier sauvegarde : ")

with open(nom_fichier + ".txt", "w") as fichier:

    mur = "#"
    chemin = "."

    mat = []
    for i in range(taille_mat):
        ligne = []  
        for j in range(taille_mat):
                ligne.append(chemin)
        mat.append(ligne)
    for ligne in mat:
        print(ligne) 
        
        fichier.write(" ".join(ligne) + "\n") 
