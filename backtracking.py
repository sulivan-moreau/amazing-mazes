import random

CHAR_GROUND = "."
CHAR_WALL = "#"
CHAR_WAY = "O"
CHAR_FAKE = "*"

DIRECTIONS = [(2, 0), (-2, 0), (0, -2), (0, 2)]
DIRECTIONS_SOLVER = [(1, 0), (-1, 0), (0, -1), (0, 1)]

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
    maze_rec(x, y)
    return m


def is_valid_neighbor(m, n, x, y):
    return 0 <= x < n and 0 <= y < n and m[x][y] == CHAR_WALL


def save_file(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "w") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")
            
def print_maze(maze):
    for line in maze:
        print(" ".join(line))

###############################################################################
def is_valid_way(m, n, x, y):
    return 0 <= x < n and 0 <= y < n and m[x][y] == CHAR_GROUND


def solve_maze(maze, n):
    m = maze
    x, y = 1, 0

    def solve_rec(x, y):
        if x == n - 2 and y == n - 1:
            m[x][y] = CHAR_WAY
            return True

        m[x][y] = CHAR_WAY

        for dx, dy in DIRECTIONS_SOLVER:
            new_pos = [x + dx, y + dy]
            if is_valid_way(m, n, new_pos[0], new_pos[1]):
                if solve_rec(new_pos[0], new_pos[1]):
                    return True

        m[x][y] = CHAR_FAKE
        return False

    solve_rec(x, y) 
    return m


def print_maze_solve(m):
    for line in m:
        print(" ".join(line))


def main_backtracking():
    n = get_matrix_size() * 2 + 1
    maze = generate_maze(n)
    print_maze(maze)
    save_file(maze)
    solver_maze = solve_maze(maze, n)
    print_maze_solve(solver_maze)
    save_file(solver_maze)

if __name__ == "__main__":
    main_backtracking()
