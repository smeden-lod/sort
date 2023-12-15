# sort

## tri sélection
Le script tri-sélection est composé de trois fonctions :
- `imini(t)` : donne l'index du minimum du tableau t donné
- `swap(t, i, j)` : inverse les objets aux indices i et j dans le tableau t
- `tri_selection(t)` : trie le tableau t donné dans l'ordre croissant

`imini(t)` est une fonction qui prend en entrée un tableau t, et renvoie *l'index* de l'entier minimal dans la liste. Elle est utilisée dans la fonction `tri_selection()`.

`swap(t, i, j)` est une fonction qui prend en entrée un tableau t et deux entiers, i et j. Ces deux entiers i et j sont définis tels que `0 <= i <len(t)`

`tri_selection(t)` est une fonction de tri *en place*, c'est à dire qu'elle modifie la liste passée, en ne créeant pas de nouvelle liste à renvoyer à l'utilisateur. Elle va modifier la liste à l'aide de `swap()`, en trouvant l'indice du minimum avec `imini()`, en le mettant au début (c'est à dire, au début du programme, t[0]), et boucler sur la liste jusqu'a que la liste soit triée, en ignorant à chaque fois les valeurs qu'on a défini dans les itérations précédentes :
`
for k in range(len(t)): # Boucle sur les éléments de t
    i = imini(t[k:]) # Récupère l'index du minimum *sur la slice t[k:]*, ignorant les nombres des itérations précédentes
    swap(t, k, i + k) # Inverse les nombres trouvés, convertissant l'index i (qui est valable uniquement sur t[k:]) en un index qui marche dans t
`