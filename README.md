# sort

## Tri sélection

Trois principales fonctions :

### Fonction `imini`

Cette fonction va parcourir **la liste d'entiers** que l'on lui donne et nous renvoyer le *premier indice* de **la plus petite valeur dans la liste**.

### Fonction `swap`

Cette fonction a pour but d'échanger deux valeurs dans une liste d'entier superieur à 2, elle va prendre la **valeur à l'indice** `i` puis l'échanger avec la **valeur à l'indice** `j`.

### Fonction `tri_selection`

La fonction tri s'occupe de la liste en elle-même, c'est elle qui va utiliser les deux fonctions précédantes afin de trier **un tableau d'entier de longueur supérieur à 2**.
A chaque boucle de cette fonction, la fonction `imini` seras appelée et donneras l'indice de la plus petite valeur dans le tableau. **Puis** la fonction `swap` va se charger de d'échanger la valeur a l'indice reçu à **l'indices 0**, puis à **l'indice 1** pour la boucle suivante jusqu'à la fin de la liste.
