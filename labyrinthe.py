wall = "#"
passs= "."

def create_list():
    nb_enter = int(input())
    name_file = input()
    
    matrice = [[wall]*nb_enter for _ in range(nb_enter)]
    
    for ligne in matrice:
        print(ligne,"\n")
        
    f = open("new_file.txt","w")
    for ligne in matrice:
        for i in ligne:
            f.write(i)
    
create_list()