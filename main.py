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
    m[-1][-1] = CHAR_GROUND
    m[-2][-1] = CHAR_GROUND 
    m[0][0] = CHAR_GROUND
    m[1][0] = CHAR_GROUND

    return m

def generate_maze(n):
    m = generate_basic_matrix(n)
    x, y = 0, 0
    n = len(m)

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

    maze_rec(1, 1)
    return m

def is_valid_neighbor(m, n, x, y):
    return 0 <= x < n and 0 <= y < n and m[x][y] == CHAR_WALL

def save_file(m):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for ligne in m:
            file.write("".join(ligne) + "\n")


        
###############################################################################################


def is_valid_way(m, n, x, y):
    # if m[x][y] == CHAR_FAKE
    return 0 <= x < n and 0 <= y < n and m[x][y] == CHAR_GROUND
    
def solve_maze(maze, n):
    m = generate_maze(n)
    l=[]
    x, y = 0, 0
    
    def solve_rec(x, y):
        if x == n - 2 and y == n - 2:
            m[x][y] = CHAR_WAY
            return False

        random.shuffle(DIRECTIONS_SOLVER)
        m[x][y] = CHAR_WAY
        for dx, dy in DIRECTIONS_SOLVER:
            new_pos = [x + dx, y + dy]
            print("x="x, "y="y, "dx="dx, "dy="dy)
            if is_valid_way(m, n, new_pos[0], new_pos[1]) and not (x == n - 2 and y == n - 2):
                # if not solve_rec(new_pos[0], new_pos[1]):
                    # return False
                solve_rec(new_pos[0], new_pos[1])
 
    solve_rec(x,y)
    return m 

# def fake_way(m, n, x, y):
#     while not is_valid_way():
#         m[x][y] = CHAR_FAKE
#         l.pop(1)
#         return 

def print_maze_solve(solver):
    for line in solver:
        print(" ".join(line))
        
###############################################################################################


def main():
    n = get_matrix_size() * 2 + 1
    maze = generate_maze(n)
    solver_maze = solve_maze(maze, n)
    print_maze_solve(solver_maze)
    #save_file(maze)
    


if __name__ == "__main__":
    main()