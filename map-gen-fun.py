import os
import time
import random

# Initialization of basic constants
WALL = "#"
FLOOR = "."
SPAWN = "S"
EXIT = "E"

def intialize_matrix(matrix_size):
    maze = [[WALL for _ in range (matrix_size * 2 + 1)] for _ in range (matrix_size * 2 + 1)]
    return maze

def recursive_backtrack(maze, x, y):
    maze[y][x] = FLOOR


def generate_matrix():
    # Input User
    matrix_size = int(input("Enter number to generate matrix: "))

    # Different lines to generate matrix template 
    border_line = [WALL] * (matrix_size * 2 + 1)
    spawn_line = [WALL] + [SPAWN] + (((matrix_size - 1) * 2) * [FLOOR]) + [WALL]
    exit_line = [WALL] + (((matrix_size - 1) * 2) * [FLOOR]) + [EXIT] + [WALL]
    empty_line = [WALL] + ((matrix_size * 2 - 1) * [FLOOR]) + [WALL]
    matrix = [border_line] + [spawn_line] + (matrix_size - 1) * [empty_line] + [exit_line] + [border_line]

    # Save template in file text
    file_name = input("Write the name of your map without spaces: ")
    with open(f"{file_name}.txt", "a") as file:
        for line in matrix:
            file.write("".join(line) + "\n")
    
    return file_name

def remove(file_name):
    path = f"{file_name}.txt"
    if os.path.isfile(path):
        os.remove(path)
        print(f"{file_name}.txt has been removed")
    else:
        print(f"{file_name}.txt does not exist")

if __name__ == "__main__":
    name_matrix = generate_matrix()
    time.sleep(10)
    remove(name_matrix)
