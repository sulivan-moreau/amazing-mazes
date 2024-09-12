import random 

def generate_matrix():
    blocked_wall = "@"
    wall = "#"
    path = "."
    entrance = "E"
    exit_point = "S"

    matrix_size = int(input("Matrix size: "))
    matrix_size = (matrix_size * 2) + 1

    mat = [[wall for _ in range(matrix_size)] for _ in range(matrix_size)]

    for i in range(matrix_size):
        mat[0][i] = blocked_wall
        mat[matrix_size - 1][i] = blocked_wall
    for i in range(matrix_size):
        mat[i][0] = blocked_wall
        mat[i][matrix_size - 1] = blocked_wall

    mat[1][1] = entrance
    exit_x, exit_y = matrix_size - 2, matrix_size - 2

    generate_backtracking_path(mat, 1, 2)

    mat[exit_x][exit_y] = exit_point

    for line in mat:
        print(" ".join(line))

    return mat

def valid_neighbor(mat, x, y):
    matrix_size = len(mat)
    return 1 <= x < matrix_size - 1 and 1 <= y < matrix_size - 1 and mat[x][y] == "#"

def get_neighbors(mat, x, y):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if valid_neighbor(mat, nx, ny):
            neighbors.append((nx, ny))
    return neighbors

def generate_backtracking_path(mat, x, y):
    stack = [(x, y)]
    mat[x][y] = "."
    
    while stack:
        print(stack)
        x, y = stack[-1]
        neighbors = get_neighbors(mat, x, y)
        
        if not neighbors:
            stack.pop()
        else:
            nx, ny = random.choice(neighbors)
            mat[nx][ny] = "."
            mat[(x + nx) // 2][(y + ny) // 2] = "."
            stack.append((nx, ny))

def save_to_file(mat):
    file_name = input("Save file name: ")
    with open(file_name + ".txt", "w") as file:
        for line in mat:
            file.write(" ".join(line) + "\n")

if __name__ == "__main__":
    matrix = generate_matrix()
    save_to_file(matrix)
