import os
import time

# Inilialization of basics variables
wall = "#"
floor = "."
spawn = "S"
exit = "E"

def matrix():
    input_user = int(input("Enter number to generate matrix : "))
    border = [wall] * (input_user * 2 + 1)
    spawn_line = [wall] + [spawn] + (((input_user - 1) * 2) * [floor]) + [wall]
    exit_line = [wall] + (((input_user - 1) * 2) * [floor]) + [exit] + [wall]
    basic_line = [wall] + ((input_user * 2 - 1) * [floor]) + [wall]
    matrix = [border] + [spawn_line] + (input_user +1) * [basic_line] + [exit_line] + [border]
    file_name = input("Write the name of your map without space : ")
    file = open(f"{file_name}.txt", "a")
    for line in matrix:
        file.write("".join(line) + "\n")
    file.close()
    return file_name

def remove(file_name):
    path = f"{file_name}.txt"
    os.remove (path)
    print(f"{file_name}' has been remove")

if __name__ == "__main__":
    name_matrix = matrix()
    time.sleep(10)
    remove(name_matrix)