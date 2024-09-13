import random
from colorama import Fore, Style
CHAR_GROUND = "."
CHAR_WALL = "#"
DIRECTIONS = [(2,0),(-2,0),(0,-2),(0,2)]

def get_matrix_size():
    while True:
        try:
            n = int(input("Size : "))
            print(type(n))
            return n
        except Exception:
            print(f"{Fore.RED}To enter the map size please enter a number{Style.RESET_ALL}")
        
def generate_basic_matrix(n): 
    m = []
    print(range (n*2),type(n),"Print de NNNN")
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
    pos = [1,1]
    
    def maze_rec(rank):
        if pos == [n*2,n*2] or rank == 50:
            return
        random.shuffle(DIRECTIONS)
        for dx, dy in DIRECTIONS:
            pos[0] += dx
            pos[1] += dy
            if valid_neighbor(m,pos[0], pos[1]) == True:   
                m[0][1] = CHAR_GROUND
                maze_rec(rank+1)
                
    maze_rec(0)
    return m

def valid_neighbor(m, x, y):
    matrix_size = len(m)
    print(x,y,"XXXXXXXXXXXXXX YYYYYYYYYYYYYYYYYYYYYYY")
    return 1 <= x < matrix_size - 1 and 1 <= y < matrix_size - 1 and m[x][y] == CHAR_WALL



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
