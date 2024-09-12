from colorama import Fore, Style
CHAR_GROUND = "."
CHAR_WALL = "#"

def size_matrice():
    n = input("Map size : ")
    if n.isnumeric()==True:
        n = int(n)
        valid = f"{Fore.GREEN}Valid map size{Style.RESET_ALL}"
        print(valid)
        return n
    else: 
        error = f"{Fore.RED}To enter the map size please enter a number{Style.RESET_ALL}"
        print(error)
        size_matrice()

def generate_maze():
    n = size_matrice()
    m = []
    for _ in range((n *2)+1):
        m.append([CHAR_WALL] * ((n *2)+1))

    # entrée et sortie
    # m[1][0] = CHAR_GROUND
    m[1][1] = CHAR_GROUND
    m[-2][-2] = CHAR_GROUND
    # m[-2][-1] = CHAR_GROUND

    for ligne in m:
        print(" ".join(ligne))

    return m

def sauvegarde_fichier(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")
            
created_maze = generate_maze()
sauvegarde_fichier(created_maze)

