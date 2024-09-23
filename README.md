# amazing-mazes

## Table des matières

- [Table des matières](#table-des-matières)
  - [L'équipe](#léquipe)
  - [Download requirements](#download-requirements)
  - [Contexte](#contexte)

## L'équipe

3 étudiants en 2ère année de `Bachelor IT spécialité Intelligence Artificielle` à [La Plateforme\_](https://laplateforme.io/) à Marseille, voici le sujet : [Amazing Mazes](https://drive.google.com/file/d/1vO0qkPHhB5dNDG89fNQi0YCuu21-_zGC/view)

- Antoine Gobbe
  <a href="https://github.com/NovaStarmax">
  <img src="img/github.png" width=25>
  </a>

- Ines Lorquet
  <a href="https://github.com/ines-lorquet">
  <img src="img/github.png" width=25>
  </a>

- Sulivan Moreau
  <a href="https://github.com/sulivan-moreau">
  <img src="img/github.png" width=25>
  </a>

## Download requirements

Installer la librairie nécessaire pour le bon fonctionnement du projet :

- Cela permet d’ajouter de la couleur dans le terminal.

```sh
pip install colorama
```

## Contexte

> Nous allons vous présenter une création et une résolution de labyrinthe à l'aide du backtracking et du krustal

> La logique de programmation sera expliqué lors de la soutenance

- Voici les algorithmes :

### Algorithmes du backtracking

Le backtracking est une technique de résolution de problèmes qui :

 - Construit progressivement une solution.
 - Teste si la solution partielle respecte les contraintes.
 - Si oui, continue à construire.
 - Si non, revient en arrière et essaie une autre option.
 - Répète jusqu'à trouver une solution complète ou épuiser toutes les possibilités.

En essence, c'est une méthode d'essai-erreur systématique qui explore l'espace des solutions en reculant dès qu'une impasse est rencontrée. Elle est souvent utilisée pour résoudre des puzzles, des problèmes de satisfaction de contraintes ou pour générer des structures comme des labyrinthes.

### L'algorithme de Kruskal

L'algorithme de Kruskal est utilisé pour trouver l'arbre couvrant minimum (MST) d'un graphe pondéré. Il fonctionne ainsi :

 - Tri : Trie toutes les arêtes du graphe par poids croissant.
 - Sélection : Ajoute les arêtes les plus légères à l'arbre couvrant, une par une.
 - Cycle : Ignore les arêtes qui forment un cycle.
 - Complet : Répète jusqu'à ce que l'arbre couvrant inclue tous les sommets.

En résumé, Kruskal construit un MST en ajoutant les arêtes les moins coûteuses tout en évitant les cycles, jusqu'à ce que tous les sommets soient connectés. C'est efficace pour les graphes clairsemés.


### L'algorithme de A Star *

L'algorithme A* (A star) est une méthode pour trouver le chemin le plus court entre deux points. Il fonctionne en explorant les chemins possibles de manière intelligente, en priorisant ceux qui semblent les plus prometteurs.

 1. Départ : On commence au point de départ.
 2. Listes ouverte et fermée :
 - -La liste ouverte contient les points à explorer.
 - -La liste fermée contient les points déjà explorés.
 3. Choix du prochain point : On examine les points voisins du point actuel et on choisit celui qui semble le plus proche de l'objectif tout en tenant compte du chemin parcouru.
 4. Réitération : Le point choisi est déplacé dans la liste fermée, et ses voisins non explorés sont ajoutés dans la liste ouverte.
 5. Arrivée : Le processus continue jusqu'à atteindre le point d'arrivée ou jusqu'à ce que tous les chemins possibles aient été explorés.

L'algorithme cherche à éviter de passer par des chemins trop longs en se basant sur une estimation de la distance restante, tout en tenant compte de la distance déjà parcourue.