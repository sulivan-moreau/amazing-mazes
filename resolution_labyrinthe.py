import generation_matrice

def liste_voisin():
    n,p = len(mat), len(mat[0])
    (a,b) = sommet 
    logigue_chemin = [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]
    tester_voisin = [i, j] for (i,j) in logigue_chemin if 0<=i<n and 0<=j<p and mat[i,j] == "#"]
    return tester_voisin 
print(liste_voisin(mat,))