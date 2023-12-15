# sort

## tri sélection
Le script tri-sélection est composé de trois fonctions :
- `imini(t)` : donne l'index du minimum du tableau t donné
- `swap(t, i, j)` : inverse les objets aux indices i et j dans le tableau t
- `tri_selection(t)` : trie le tableau t donné dans l'ordre croissant

`tri_selection(t)` est une fonction de tri *en place*, c'est à dire qu'elle modifie les éléments de la liste passée, en ne créeant pas de nouvelle liste à renvoyer à l'utilisateur. Elle va modifier la liste à l'aide de `swap()`, en trouvant l'indice du minimum avec `imini()` et en le mettant à la première place, c'est à dire `t[0]`