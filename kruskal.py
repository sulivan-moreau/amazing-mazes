import random

CHAR_GROUND = "."
CHAR_WALL = "#"
DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def get_matrix_size():
    while True:
        try:
            n = int(input("Size : "))
            return n
        except ValueError:
            print("To enter the map size please enter a number")

def generate_basic_matrix(n):
    m = [[CHAR_WALL] * (n * 2 + 1) for _ in range(n * 2 + 1)]
    return m

def generate_maze(n):
    m = generate_basic_matrix(n)
    cells = []
    for x in range(1, n * 2, 2):
        for y in range(1, n * 2, 2):
            m[x][y] = CHAR_GROUND
            cells.append((x, y))

    def get_neighbors(cell):
        x, y = cell
        neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < len(m) - 1 and 0 < ny < len(m[0]) - 1:
                neighbors.append((nx, ny))
        return neighbors

    return m

def print_maze(maze):
    for line in maze:
        print(" ".join(line))

def main():
    n = get_matrix_size()
    maze = generate_maze(n)
    print_maze(maze)

if __name__ == "__main__":
    main()