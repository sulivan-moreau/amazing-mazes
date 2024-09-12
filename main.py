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


def generate_maze(n):
    m = []
    for _ in range(n * 2 + 1):
        m.append([CHAR_WALL] * (n * 2 + 1))

    # entrée et sortie
    m[1][0] = CHAR_GROUND
    m[1][1] = CHAR_GROUND
    m[-2][-2] = CHAR_GROUND
    m[-2][-1] = CHAR_GROUND

    return m


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
