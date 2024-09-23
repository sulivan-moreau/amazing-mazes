from backtracking import main_backtracking
from kruskal import main_kruskal

print("Welcome to Amazing Maze, you have to select algoritme to generate maze.")
file_choice = input("1 : Backtracking , 2 : Kruskal  :  ")

if file_choice == "1":
    main_backtracking()

elif file_choice == "2":
    main_kruskal()
    