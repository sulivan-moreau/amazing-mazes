def generation():
    
    mur = "#"
chemin = "."
entree = "E"
sortie = "S"

taille_mat = int(input("Taille de la matrice : "))

mat = []
for i in range(taille_mat):
        ligne = []  
        for j in range(taille_mat):
            ligne.append(chemin)
        mat.append(ligne)

mat[taille_mat -1 ][taille_mat -1 ] = sortie
mat[0][0] = entree
            
#for ligne in mat:
            #print(ligne) 
            
generation()

   

#nom_fichier = input("Fichier sauvegarde : ")          
#nom_fichier with open(nom_fichier + ".txt", "w") as fichier:
#fichier.write(" ".join(ligne) + "\n") 