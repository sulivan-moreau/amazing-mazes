import random
# from colorama import Fore, Style
CHAR_GROUND = "."
CHAR_WALL = "#"

# def nouvelle():
#     while True:
#         try :
#             n = int(input())


def get_matrix_size():
    n = input("Map size : ")
    if n.isnumeric() == True:
        n = int(n)
        # valid = f"{Fore.GREEN}Valid map size{Style.RESET_ALL}"
        #  print(valid)
        return n
    else:
        # error = f"{Fore.RED}To enter the map size please enter a number{Style.RESET_ALL}"
        # print(error)
        return get_matrix_size()

def generate_basic_matrix(n): 
    m = []
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
    directions = [(2,0),(-2,0),(0,-2),(0,2)]
    random.shuffle(directions)
    print(directions)
    pos = [1,1]
    for dx, dy in directions:
        pos[0] += dx
        pos[1] += dy
        if m[pos[0]][pos[1]] == CHAR_WALL:
            m[0][1] = CHAR_GROUND

def valid_neighbor(mat, x, y):
     matrix_size = len(mat)
     return 1 <= x < matrix_size - 1 and 1 <= y < matrix_size - 1 and mat[x][y] == "#"

 if voisin_valide(mat, nx, ny):
             mat[x + dx // 2][y + dy // 2] = "."
             mat[nx][ny] = "."

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
    save_file(maze)


if __name__ == "__main__":
    main()
