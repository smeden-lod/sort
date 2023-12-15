# sort

On cherche à ranger dans l'ordre (croissant) des collections objets. Cela peut être des `int`, des `str`, des `tuple` de `int`. On peut appliquer ces algorithmes à toute collection d'objets *ordonnables*, c'est-à-dire d'objets sur lesquels la fonction `a, b -> a < b` est définie. 

Les collections sont des *tableaux statiques*. En python, on travaille avec des `list` mais on impose que tous les éléments aient le même type et on s'interdit les méthodes `append` et `pop`.

Les tris suivants sont des tris *en place* : ils modifient le tableau passé en paramètre. Des versions plus *fonctionnelles* produisent un nouveau tableau rangé dans l'ordre.

## tri sélection

## tri insertion