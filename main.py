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
    for _ in range(n * 2 + 1):
        m.append([CHAR_WALL] * (n * 2 + 1))

    # entrée et sortie
    # m[1][0] = CHAR_GROUND
    m[1][1] = CHAR_GROUND
    m[-2][-2] = CHAR_GROUND
    # m[-2][-1] = CHAR_GROUND

    return m


def generate_maze(n):
    m = generate_basic_matrix(n)
    x, y = 1,1   
    
    def maze_rec(x, y, rank):
        print(m[2 * n -1][2 *n - 1])
        if x == n * 2 - 1 and y == n * 2 - 1:
            print("ENNNNDD")
            return True

        random.shuffle(DIRECTIONS)
        m[x][y] = CHAR_GROUND
        
        for dx, dy in DIRECTIONS:
            new_pos = [x + dx, y+ dy]
            if valid_neighbor(m, new_pos[0], new_pos[1], rank):

                m[x + dx // 2][y + dy // 2] = CHAR_GROUND
                # pos[0], pos[1] = new_pos[0], new_pos[1]
                if maze_rec(new_pos[0],new_pos[1],rank + 1):
                    return True

                # return rank
            # elif new_pos == [n * 2-1 , n * 2-1]:
            #     m[new_pos[0] - dx // 2][new_pos[1] - dy // 2] = CHAR_GROUND
            #     print("sdfghjik")
        return False
    maze_rec(1, 1, 0)
    return m

def valid_neighbor(m, x, y, rank):
    matrix_size = len(m)
    # val = 0 <= x < matrix_size and 0 <= y < matrix_size and m[x][y] == CHAR_WALL
    print("Étape ", rank, " : X=", x, ", Y=", y)

    return (
        0 <= x < matrix_size and 0 <= y < matrix_size and m[x][y] == CHAR_WALL
    )


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
