def generation():
    taille_mat = int(input("Taille de la matrice : "))
    mur = "#"
    chemin = "."
    porte = "P"

    mat = []
    for i in range(taille_mat):
        ligne = []  
        for j in range(taille_mat):
            ligne.append(chemin)
        mat.append(ligne)
        
    mat[0][0] = porte
    mat[taille_mat -1 ][taille_mat -1 ] = porte
    
            
    for ligne in mat:
            print(ligne) 

generation()



#nom_fichier = input("Fichier sauvegarde : ")          
#nom_fichier with open(nom_fichier + ".txt", "w") as fichier:
#fichier.write(" ".join(ligne) + "\n") 