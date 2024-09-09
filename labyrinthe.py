wall = "#"
passs= "."

def create_list():
    nb_enter = int(input())
    name_file = input("Nom du fichier : ")
    
    matrice = [[wall]*nb_enter for _ in range(nb_enter)]
    matrice[0][0] = passs
    matrice[nb_enter-1][nb_enter-1] = passs
    
    for ligne in matrice:
        print(ligne,"\n")

    with open(f'{name_file}.txt', 'w') as file:
        for ligne in matrice:
            file.write(''.join(ligne) + '\n')
                
create_list()