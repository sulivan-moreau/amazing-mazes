import random
from colorama import Fore, Style
CHAR_GROUND = "."
CHAR_WALL = "#"

def get_matrix_size():
    while True:
        try:
            n = int(input())
            
            return n
        except Exception:
            print(f"{Fore.RED}To enter the map size please enter a number{Style.RESET_ALL}")
        
def generate_basic_matrix(n): 
    m = []
    print(n,"sdfghujikolmù")
    for _ in range(n * 2 + 1):
        m.append([CHAR_WALL] * (n * 2 + 1))

    # entrée et sortie
    m[1][0] = CHAR_GROUND
    m[1][1] = CHAR_GROUND
    m[-2][-2] = CHAR_GROUND
    m[-2][-1] = CHAR_GROUND

    return m


def generate_maze(n):
    # La parti récursive doit pas être à chaque fois m 
    m = generate_basic_matrix(n)
    print(n,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    directions = [(2,0),(-2,0),(0,-2),(0,2)]

    random.shuffle(directions)
    pos = [1,1]
    for dx, dy in directions:
        pos[0] += dx
        pos[1] += dy
        if m[pos[0]][pos[1]] == CHAR_WALL:
            m[0][1] = CHAR_GROUND
             
    return m

def valid_neighbor(m, x, y):
    matrix_size = generate_maze(m)
    matrix_size = len(m)
    print(x,y,"XXXXXXXXXXXXXX YYYYYYYYYYYYYYYYYYYYYYY")
    return 1 <= x < matrix_size - 1 and 1 <= y < matrix_size - 1 and m[x][y] == "#"



def save_file(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")

def print_maze(maze):
    for line in maze:
        print(" ".join(line))


def main():
    n = get_matrix_size()
    maze = generate_maze(n)

    print_maze(maze)
    # save_file(maze)


if __name__ == "__main__":
    main()
