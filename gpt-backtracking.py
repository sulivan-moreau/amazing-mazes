import os
import time
import random

# Constants
WALL = "#"
FLOOR = "."
SPAWN = "S"
EXIT = "E"

# Generate matrix of wall with input of user
def initialize_maze(matrix_size):
    maze = [[WALL for _ in range(matrix_size * 2 + 1)] for _ in range(matrix_size * 2 + 1)]
    return maze

# Fonction récursive pour générer un labyrinthe avec le backtracking
def recursive_backtrack(maze, x, y):
    maze[y][x] = FLOOR  # Définir la cellule actuelle comme un chemin
    
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Déplacement de 2 cellules (droite, gauche, bas, haut)
    random.shuffle(directions)  # Mélanger les directions pour un labyrinthe aléatoire

    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # Nouvelle position après déplacement

        # Vérifier que la nouvelle position est valide et n'a pas encore été visitée
        if 1 <= nx < len(maze) - 1 and 1 <= ny < len(maze) - 1 and maze[ny][nx] == WALL:
            # on vérifie que c’est compris entre 1 et la largueur max de maze car le premier et le dernier sont des murs, cela évite qu’on dépasse la taille de la matrice
            maze[ny - dy // 2][nx - dx // 2] = FLOOR  # Casser le mur entre la cellule actuelle et la prochaine
            recursive_backtrack(maze, nx, ny)  # Appel récursif pour continuer le chemin

# Ajouter les points de départ et de sortie
def add_spawn_and_exit(maze):
    maze[1][1] = SPAWN  # Point de départ en haut à gauche
    maze[-2][-2] = EXIT  # Sortie en bas à droite

def generate_maze():
    # Input User
    matrix_size = int(input("Enter number to generate maze: "))
    
    # Initialize maze filled with walls
    maze = initialize_maze(matrix_size)
    
    # Start the recursive backtracking from (1,1)
    recursive_backtrack(maze, 1, 1)
    
    # Add spawn and exit points
    add_spawn_and_exit(maze)
    
    # Save the maze to a file
    file_name = input("Write the name of your maze without spaces: ")
    with open(f"{file_name}.txt", "w") as file:
        for line in maze:
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
    name_maze = generate_maze()
    time.sleep(10)
    remove(name_maze)
