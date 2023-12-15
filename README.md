# sort

## tri sélection
L'algorithme `tri_selection()` permet de trier **dans l'ordre croissant** un *tableau d'entiers* donné en entrée.
Pour y parvenir, celui-ci fait appelle aux fonctions :
- `imini()` : qui renvoie l'indice de la valeur minimum dans un *tableau d'entiers*.
- `swap()` : qui échange les valeurs aux 2 indices donnés en entrée dans un *tableau d'entiers*.

Cet algorithme va énumérer chaque entier présent dans le tableau donné, puis va échanger chacune de ces valeurs (`swap()`) avec la valeur minimum du tableau (`imini()`).
Une fois que tous les éléments ont été échangé, le tableau retourné est bel-et-bien dans l'ordre croissant.