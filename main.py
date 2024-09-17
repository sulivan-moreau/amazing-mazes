import random

CHAR_GROUND = "."
CHAR_WALL = "#"
DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def get_matrix_size():
    while True:
        try:
            n = int(input("Size : "))
            return n
        except Exception:
            print("To enter the map size please enter a number")


def generate_basic_matrix(n):
    m = []
    for _ in range(n * 2 + 1):
        m.append([CHAR_WALL] * (n * 2 + 1))
    return m


def generate_maze(n):
    m = generate_basic_matrix(n)
    x, y = 1, 1

    for i in range(n):
        y = 1
        m[x][y] = CHAR_GROUND
        for i in range(n):
            m[x][y] = CHAR_GROUND
            y += 2
        x += 2
        


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
