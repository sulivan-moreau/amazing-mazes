import os
import time

def main():
    # Intialisation des variables
    cote_carre = int(input("Rentrez un nombre pour générer une matrice : "))
    mur = "#"
    sol = "."
    entre = "E"
    sortie = "S"

    # Création des lignes
    ligne_debut = [entre] + [mur] * (cote_carre - 1)
    ligne_mur = [mur] * cote_carre 
    ligne_fin = [mur] * (cote_carre - 1) + [sortie]

    # Création de la matrice
    matrice = [ligne_debut] + [ligne_mur] * (cote_carre - 2) + [ligne_fin]

    # Création du fichier txt
    nom_fichier = input("Veuillez nommer votre carte sans espace : ")
    fichier = open(f"{nom_fichier}.txt", "a")
    for ligne in matrice:
        fichier.write("".join(ligne) + "\n")
    fichier.close()

    # Retourne le fichier txt
    return nom_fichier

# Fonction de supression du fichier txt
def supr(nom_fichier):
    chemin = f"{nom_fichier}.txt"

    if os.path.isfile(chemin) :
        os.remove (chemin)
        print(f"Le fichier '{chemin}' a été supprimé")
    else:
        print(f"Le fichier '{chemin}' n'existe pas")

def gen_map(): 
    while 


if __name__ == "__main__":
    nom_fichier_cree = main()
    time.sleep(4)
    supr(nom_fichier_cree)