import os

def main():
    # Intialisation des variables
    mur = "#"
    sol = "."

    # Génération de la map
    cote_carre = int(input("Rentrez un nombre pour générer une matrice : "))

    matrice = [[mur] * cote_carre for _ in range (cote_carre)]
    print(matrice)
    for ligne in matrice :
        print(''.join(ligne),"\n")

    nom_fichier = input("Veuillez nommer votre carte sans espace : ")
    fichier = open(f"{nom_fichier}.txt", "a")
    for ligne in matrice:
        fichier.write("".join(ligne) + "\n")
    fichier.close()

if __name__ == "__main__":
    main()