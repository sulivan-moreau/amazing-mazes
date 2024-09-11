CHAR_GROUND = "."
CHAR_WALL = "#"

def size_matrice():
    n = input("Taille de la matrice : ")
    if n.isdigit():
        return int(n)
    else: 
        print("Réesssayez avec un chiffre")
        return size_matrice()

def generate_maze(n):
    m = []
    for _ in range(2 * n + 1):
        m.append([CHAR_WALL] * (n * 2 + 1))

    # entrée et sortie
    m[1][0] = CHAR_GROUND
    m[1][1] = CHAR_GROUND
    m[-2][-2] = CHAR_GROUND
    m[-2][-1] = CHAR_GROUND

    for ligne in m:
        print(" ".join(ligne))

    return m

def sauvegarde_fichier(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")
n = size_matrice()
created_maze = generate_maze(n)
sauvegarde_fichier(created_maze)

