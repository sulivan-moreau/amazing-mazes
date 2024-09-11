import os
import time
import random

# Initialization of basic constants
WALL = "#"
FLOOR = "."
SPAWN = "S"
EXIT = "E"

def intialize_matrix(matrix_size):
    matrix = [[WALL for _ in range (matrix_size * 2 + 1)] for _ in range (matrix_size * 2 + 1)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("".join(row))

matrix_size = int(input("Enter matrix size: "))
matrix = intialize_matrix(matrix_size)  
print_matrix(matrix)