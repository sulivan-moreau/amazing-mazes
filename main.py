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
    pos = [1, 1]
    stack = [(pos[0], pos[1])]
    
    def maze_rec(rank):
        print(stack)
        
        while stack:
            if pos == [n * 2, n * 2] or rank == 50:
                return
            random.shuffle(DIRECTIONS)
            
            for dx, dy in DIRECTIONS:
                new_pos = [pos[0] + dy, pos[1] + dx]
                if valid_neighbor(m, new_pos[0], new_pos[1], rank) == True:
                    m[new_pos[0]][new_pos[1]] = CHAR_GROUND
                    m[(pos[0] + new_pos[0]) // 2][(pos[1] + new_pos[1]) // 2] = CHAR_GROUND
                    pos[0], pos[1] = new_pos[0], new_pos[1]
                    stack.append((new_pos[0], new_pos[1]))
                    print(stack)
                    maze_rec(rank + 1)
                    return rank
                
                else:
                    stack.pop()
                    print(stack)
                    maze_rec(rank + 1)
                    return rank

    maze_rec(0)
    return m

def valid_neighbor(m, x, y, rank):
    matrix_size = len(m)
    print("Étape ", rank, " : X [", x, "]" "  Y [", y, "]")
    return (
        1 <= x < matrix_size - 1 and 1 <= y < matrix_size - 1 and m[x][y] == CHAR_WALL
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
