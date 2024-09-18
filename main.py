import random

CHAR_GROUND = "."
CHAR_WALL = "#"
DIRECTIONS = [(2, 0), (-2, 0), (0, -2), (0, 2)]


def get_matrix_size():
    while True:
        try:
            n = int(input("Size : "))
            return n
        except Exception:
            print("To enter the map size please enter a number")


def generate_basic_matrix(n):
    m = []
    for _ in range(n):
        m.append([CHAR_WALL] * (n))
    m[1][1] = CHAR_GROUND
    m[-2][-1] = CHAR_GROUND 
    return m


def generate_maze(n):
    m = generate_basic_matrix(n)
    x, y = 1, 1
    n = len(m) # Utile ? 

    def maze_rec(x, y):
        random.shuffle(DIRECTIONS)
        m[x][y] = CHAR_GROUND
        for dx, dy in DIRECTIONS:
            new_pos = [x + dx, y + dy]
            if is_valid_neighbor(m, n, new_pos[0], new_pos[1]):
                m[x + dx // 2][y + dy // 2] = CHAR_GROUND
                if maze_rec(new_pos[0], new_pos[1]):
                    return
        return
    maze_rec(1, 1) # pq (1, 1) et pas (x, y)?
    return m


def is_valid_neighbor(m, n, x, y):
    return 0 <= x < n and 0 <= y < n and m[x][y] == CHAR_WALL


def save_file(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")


def print_maze(maze):
    for line in maze:
        print(" ".join(line))


def main():
    n = get_matrix_size() * 2 + 1
    maze = generate_maze(n)
    print_maze(maze)
    save_file(maze)


if __name__ == "__main__":
    main()