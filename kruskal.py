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
    groups = []
    cells = []
    
    def build_groups():
        for x in range(1, n * 2, 2):
            for y in range(1, n * 2, 2):
                m[x][y] = CHAR_GROUND
                groups.append({(x, y)})
                cells.append((x,y))
    build_groups()
    #print("groups : ", groups)

    def get_neighbors(cell):
        x, y = cell[0],cell[1]
        neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < len(m) - 1 and 0 < ny < len(m[0]) - 1:
                neighbors.append((nx, ny))
        return neighbors

    def get_cell_group(cell):
        for group in groups:
            for ce in group:
                if ce == cell:
                    return group
        #print("cell : ", cell)
                

    def belong_to_same_group(cell_1,cell_2):
        group_1 = get_cell_group(cell_1)
        group_2 = get_cell_group(cell_2)
        return group_1 == group_2

    def merge_groups(group_1, group_2):
        print("groupe1: ", group_1)
        return group_1.union(group_2)
    
    def kruskal_generation():
        random.shuffle(cells)
        for cell in cells:
            #print("cell : ", cell)
            neighbors = get_neighbors(cell)
            random.shuffle(neighbors)
            for neighbor in neighbors:
                #print("neighbor : ", neighbor)
                if not belong_to_same_group(cell, neighbor):
                    group1 = get_cell_group(cell)
                    group2 = get_cell_group(neighbor)
                    print(group1, group2)
                    group1 = merge_groups(group1, group2)
                    groups.remove(group2)

    def apply_to_map(group):
        x1, y1 = group[0],group[1]
        x2, y2 = group[2],group[3]

        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        m[mx][my] = CHAR_GROUND
        for line in m:
            print(" ".join(line))
        return m
    
    
    kruskal_generation()
    # merge_groups(cells)
    return m

def print_maze(maze):
    for line in maze:
        print(" ".join(line))

def main():
    n = get_matrix_size()
    maze = generate_maze(n)
    print_maze(maze)

if __name__ == "__main__":
    print("---------------------------------------------------------------------------------")
    main()
    print("---------------------------------------------------------------------------------")