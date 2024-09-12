import os
import time
import random

# Initialization of basic constants
WALL = "#"
FLOOR = "."
SPAWN = "S"
EXIT = "E"

def generate_maze_template():
    input_matrix = int(input("Enter number to generate matrix: "))
    maze_template = []
    for _ in range(2 * input_matrix + 1):
        maze_template.append([WALL] * (input_matrix * 2 + 1))
    maze_template [1][1] = SPAWN
    maze_template [-2][-2] = EXIT
    return maze_template

def save_as_file(maze_template):
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for line in maze_template:
            file.write("".join(line) + "\n")
    return file_name

def remove_maze_template(file_name):
    path = f"{file_name}.txt"
    if os.path.isfile(path):
        os.remove(path)
        print(f"{file_name}.txt has been removed")
    else:
        print(f"{file_name}.txt does not exist")

def maze(maze_template, x, y):

    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    random.shuffle(directions)
    
    maze_template[x][y] = FLOOR
    digger = [1][1]


    haut = maze_template[0][+2]
    bas = maze_template[0][-2]
    gauche = maze_template[-2][0]
    droite = maze_template[+2][0]
    maze_digger = [(x,y)]
    #random.shuffle

if __name__ == "__main__":
    maze_template = generate_maze_template()
    file_name = save_as_file(maze_template)
    time.sleep(6)
    remove_maze_template(file_name)
