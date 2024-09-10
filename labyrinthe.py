# import random

# wall = "#"
# passs = "."
# nb_enter = int(input("Number enter : "))

# def create_matrice():
#     nb = (nb_enter*2)+1
#     string = wall*nb
#     matrice = [string for _ in range(nb)]
    
#     for ligne in matrice:
#         print(ligne, "\n")
#     text = matrice[0]
#     caractere = list(text)
#     caractere[0][0] = "X"
#     text = "".join(caractere)

#     return matrice

# def create_file():
#     matrice = create_matrice()
#     name_file = input("Nom du fichier : ")
    
#     # matrice[nb_enter - 1][nb_enter - 1] = passs

#     with open(f"{name_file}.txt", "w") as file:
#         for ligne in matrice:
#             file.write("".join(ligne) + "\n")

# # def modify_matrice():
    
    
# create_file()


















    # for i, ligne in enumerate(matrice):
    #     a = random.randint(0, nb_enter - 1)
    #     matrice[i][a] = passs


# random_matrice()

# def random_matrice():
#     matrice = [[wall] * nb_enter for _ in range(nb_enter)]
#     matrice[0][0] = passs
#     matrice[nb_enter - 1][nb_enter - 1] = passs

#     for i, ligne in enumerate(matrice):
#         a = random.randint(0, nb_enter - 1)
#         matrice[i][a] = passs

#     for ligne in matrice:
#         print(ligne, "\n")




# import random

# wall = "#"
# passs = "."
# nb_enter = int(input("Number enter : "))

# def create_matrice():
#     nb = (nb_enter * 2) + 1
#     string = [wall] * nb
#     matrice = [string[:] for _ in range(nb)]

#     for ligne in matrice:
#         print("".join(ligne), "\n")

#     return matrice

# def create_file():
#     matrice = create_matrice()
#     name_file = input("Nom du fichier : ")

#     with open(f"{name_file}.txt", "w") as file:
#         for ligne in matrice:
#             file.write("".join(ligne) + "\n")

# create_file()



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

    

def sauvegarde_fichier(mat):
    nom_fichier = input("Nom du fichier de sauvegarde : ")
    with open(nom_fichier + ".txt", "w") as fichier:
        for ligne in mat:
            fichier.write(" ".join(ligne) + "\n")
            
generation_matrice()